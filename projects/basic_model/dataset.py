import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


class IrisDataset(Dataset):
    def __init__(self, is_train: bool = True):
        super().__init__()
        self.df = self.prepare_data(is_train)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx: int):
        record = self.df.iloc[idx]
        # line 9에서 np.float32로 type을 바꿔준 후 torch.float로 다시 type을 바꿔줘야 함. 개선 가능한가?
        x = torch.tensor(record.iloc[:][:-1]).float()
        y = torch.tensor([0.03, 0.03, 0.03])
        y[['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'].index(record.iloc[:][-1])] += 0.91
        return x, y

    def prepare_data(self, is_train: bool):
        data = pd.read_csv('iris/iris.data', header=None, sep=',')
        data.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Label']
        data.iloc[:, :-1] = self.df.iloc[:, :-1].astype(np.float32)
        if is_train:
            return pd.concat([data.iloc[:40], data.iloc[50:90], data.iloc[100:140]], ignore_index=True)
        return pd.concat([data.iloc[40:50], data.iloc[90:100], data.iloc[140:]], ignore_index=True)


if __name__ == '__main__':
    dataset = IrisDataset(is_train=True)
    print(f"dataset[0]:\n{dataset[0]}")
    print(f"dataset[1]:\n{dataset[1]}")
    print(f"dataset[2]:\n{dataset[2]}")
    print(f"dataset[3]:\n{dataset[3]}")
    print(f"dataset[4]:\n{dataset[4]}")

