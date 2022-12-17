import torch
import numpy as np
import torch, torch.nn as nn

np.random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)


class TinyConv(nn.Module):
    def __init__(self):
        super(TinyConv, self).__init__()
        # TODO unsure about these numbers here ???
        self.conv1 = nn.Conv2d(1, 8, kernel_size=(3, 3), stride=(3, 3), padding=0)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=(3, 3), stride=(3, 3), padding=0)
        self.fc = nn.Linear(in_features=16 * 3 * 3, out_features=3)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = torch.flatten(x, start_dim=1, end_dim=-1)
        x = self.fc(x)
        out = {"out": x}
        return out
