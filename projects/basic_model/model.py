import torch
import torch.nn.functional as F


class CustomModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear0 = torch.nn.Linear(4, 16)
        self.linear1 = torch.nn.Linear(16, 3)

    def forward(self, x):
        x = F.relu(self.Lin1(x))
        return F.softmax(self.Lin2(x), dim=1)


if __name__ == "__main__":
    model = CustomModel()
    print(f"CustomModel: {model}")
    print(model.linear1.weight.dtype)
