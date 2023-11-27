import torch
import dataset

IrisTrainDataset = dataset.IrisDataset(is_train=True)
IrisTestDataset = dataset.IrisDataset(is_train=False)

# train.py에서 IrisDataLoader(is_train) 객체를 생성한 후, 인스턴스 내부의 .IrisDataLoader에 접근.
# IrisDataLoader 클래스를 따로 선언하지 않고 train.py에서 일반적인 DataLoader 클래스로 객체를 선언하는 게 더 좋을지?
class IrisDataLoader():
    def __init__(self, is_train):
        self.IrisDataset = dataset.IrisDataset(is_train=is_train)
        self.IrisDataLoader = torch.utils.data.DataLoader(self.IrisDataset, batch_size = 8, shuffle = True)


if __name__ == '__main__':
    DL = IrisDataLoader(is_train=True).IrisDataLoader
    print(f"DL[0]: {next(iter(DL))}")
