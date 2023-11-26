import torch
import dataset

IrisTrainDataset = dataset.IrisDataset(is_train=True)
IrisTestDataset = dataset.IrisDataset(is_train=False)

class IrisDataLoader():
    def __init__(self, is_train):
        self.IrisDataset = dataset.IrisDataset(is_train=is_train)
        self.IrisDataLoader = torch.utils.data.DataLoader(self.IrisDataset, batch_size = 8, shuffle = True)


if __name__ == '__main__':
    DL = IrisDataLoader(is_train=True).IrisDataLoader
    print(f"DL[0]: {next(iter(DL))}")