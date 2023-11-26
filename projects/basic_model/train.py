import torch
import model
import dataloader
import matplotlib.pyplot as plt

def main():
    IrisTrainDataLoader = dataloader.IrisDataLoader(is_train=True).IrisDataLoader
    IrisTestDataLoader = dataloader.IrisDataLoader(is_train=False).IrisDataLoader

    Model = model.CustomModel()
    optm = torch.optim.Adam(Model.parameters())
    loss_fn = torch.nn.CrossEntropyLoss()

    train_loss, train_acc, test_loss, test_acc = [], [], [], []

    for epoch in range(50):
        loss_sum, acc_sum = 0, 0
        for x, y in IrisTrainDataLoader:
            y_ = Model(x)

            optm.zero_grad()
            loss = loss_fn(y_, y)
            loss.backward()
            optm.step()

            loss_sum += loss.item()
            acc_sum += int(sum(y.argmax(dim=1) == y_.argmax(dim=1)))

        train_loss.append(loss_sum/(120/8))
        train_acc.append(acc_sum/120)

        loss_sum, acc_sum = 0,0
        with torch.no_grad():
            for x, y in IrisTestDataLoader:
                y_ = Model(x)

                loss = loss_fn(y_, y)

                loss_sum += loss.item()
                acc_sum += int(sum(y.argmax(dim=1) == y_.argmax(dim=1)))

        test_loss.append(loss_sum/(30//8))
        test_acc.append(acc_sum/30)

        if epoch%10 == 0:
            print(f"[Epochs]:{epoch}\n[Train Loss]:{train_loss[-1]}, [Train Accuracy]:{train_acc[-1]}\n[Test Loss]:{test_loss[-1]}, [Test Accuracy]:{test_acc[-1]}")

    with torch.no_grad():
        x, y = next(iter(IrisTestDataLoader))
        y_ = Model(x)

        y = [['Iris-setosa','Iris-versicolor','Iris-virginica'][idx] for idx in y.argmax(dim=1)]
        y_ = [['Iris-setosa','Iris-versicolor','Iris-virginica'][idx] for idx in y_.argmax(dim=1)]

        print(y)
        print(y_)

    fig, axes = plt.subplots(1,2)
    for i, value in enumerate(['Loss', 'Accuracy']):
        axes[i].set_title(value)
        axes[i].set_xlabel('Epochs')
        if value == 'Loss':
            axes[i].plot(train_loss, label = 'Train')
            axes[i].plot(test_loss, label = 'Test')
        else:
            axes[i].plot(train_acc, label = 'Train')
            axes[i].plot(test_acc, label = 'Test')
        axes[i].legend()
    fig.savefig('result')

main()