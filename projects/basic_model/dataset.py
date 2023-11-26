import pandas as pd
import torch
import numpy as np

class IrisDataset(torch.utils.data.Dataset):
    def __init__(self, is_train):
        self.df = pd.read_csv('iris/iris.data', header=None, sep=',')
        self.df.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Label']
        self.df.iloc[:,:-1] = self.df.iloc[:,:-1].astype(np.float32)
        if is_train == True:
            self.df = pd.concat([self.df.iloc[:40], self.df.iloc[50:90], self.df.iloc[100:140]], ignore_index=True)
        elif is_train == False:
            self.df = pd.concat([self.df.iloc[40:50], self.df.iloc[90:100], self.df.iloc[140:]], ignore_index=True)
        else:
            raise RuntimeError

    def __len__(self):
        return len(self.df)
    
    def __getitem__(self,idx):
        record = self.df.iloc[idx]
        x = torch.tensor(record.iloc[:][:-1]).type(torch.float)
        y = torch.tensor([0.03, 0.03, 0.03])
        y[['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'].index(record.iloc[:][-1])] += 0.91
        return x, y

if __name__ == '__main__':
    DS = IrisDataset(is_train=True)
    print(f"DS[0]:\n{DS[0]}")
    print(f"DS[1]:\n{DS[1]}")
    print(f"DS[2]:\n{DS[2]}")
    print(f"DS[3]:\n{DS[3]}")
    print(f"DS[4]:\n{DS[4]}")
    