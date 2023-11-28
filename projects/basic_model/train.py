import torch
from torch import nn, optim
from torch.optim import Optimizer
from model import CustomModel
from torch.utils.data import DataLoader
from dataset import IrisDataset
import matplotlib.pyplot as plt


def train_one_epoch(model: nn.Module, dataloader: DataLoader, optimizer: Optimizer, loss_fn: nn.Module):
    loss_sum, acc_sum = 0, 0
    for x, y_true in dataloader:
        y_pred = model(x)

        optimizer.zero_grad()
        loss = loss_fn(y_pred, y_true)
        loss.backward()
        optimizer.step()

        loss_sum += loss.item()
        acc_sum += int(sum(y_true.argmax(dim=1) == y_pred.argmax(dim=1)))

    loss = loss_sum / (120 / 8)
    acc = acc_sum / 120
    return loss, acc


def test_one_epoch(model: nn.Module, dataloader: DataLoader, loss_fn: nn.Module):
    loss_sum, acc_sum = 0, 0
    with torch.no_grad():
        for x, y_true in dataloader:
            y_pred = model(x)
            loss = loss_fn(y_pred, y_true)
            loss_sum += loss.item()
            acc_sum += int(sum(y.argmax(dim=1) == y_.argmax(dim=1)))
    loss = loss_sum / (30 / 8)
    acc = acc_sum / 30
    return loss, acc


def main():
    train_dataset = IrisDataset()
    test_dataset = IrisDataset(is_train=False)

    train_dataloader = DataLoader(train_dataset, batch_size=8)
    test_dataloader = DataLoader(test_dataset, batch_size=8)

    model = CustomModel()
    optimizer = optim.Adam(model.parameters())
    loss_fn = nn.CrossEntropyLoss()

    train_loss, train_acc, test_loss, test_acc = [], [], [], []

    for epoch in range(50):
        train_epoch_loss, train_epoch_acc = train_one_epoch(model, train_dataloader, optimizer, loss_fn)
        test_epoch_loss, test_epoch_acc = test_one_epoch(model, test_dataloader, loss_fn)
        # Print Loss and Accuracy
        if epoch % 10 == 0:
            print(
                f"[Epochs]:{epoch}\n"
                f"[Train Loss]:{train_epoch_loss}, "
                f"[Train Accuracy]:{train_epoch_acc}\n"
                f"[Test Loss]:{test_epoch_loss}, "
                f"[Test Accuracy]:{test_epoch_acc}"
            )
        train_loss.append(train_epoch_loss)
        train_acc.append(train_epoch_acc)
        test_loss.append(test_epoch_loss)
        test_acc.append(test_epoch_acc)

    # Print Label and Prediction
    with torch.no_grad():
        x, y_true = next(iter(test_dataloader))
        y_pred = model(x)

        y_true = [
            ["Iris-setosa", "Iris-versicolor", "Iris-virginica"][idx]
            for idx in y.argmax(dim=1)
        ]
        y_pred = [
            ["Iris-setosa", "Iris-versicolor", "Iris-virginica"][idx]
            for idx in y_.argmax(dim=1)
        ]

        print(y_true)
        print(y_pred)

    # Save Fig.
    fig, axes = plt.subplots(1, 2)
    for i, value in enumerate(["Loss", "Accuracy"]):
        axes[i].set_title(value)
        axes[i].set_xlabel("Epochs")
        if value == "Loss":
            axes[i].plot(train_loss, label="Train")
            axes[i].plot(test_loss, label="Test")
        else:
            axes[i].plot(train_acc, label="Train")
            axes[i].plot(test_acc, label="Test")
        axes[i].legend()
    fig.savefig("result")


main()
