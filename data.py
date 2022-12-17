import os
import PIL
import torch
import pandas as pd
from torch.utils.data import Dataset
from torchvision import transforms


class ReportCards(Dataset):
    def __init__(self, set: str):
        self.dir = os.path.join(os.getcwd(), "norm", set)
        self.cards = os.listdir(self.dir)
        self.labels = pd.read_excel(
            os.path.join(os.getcwd(), "labels-smile.xlsx"), header=0, index_col=0
        )
        self.attributes = self.labels.columns.values.tolist()
        self.label_meanings = self.attributes
        print(f"label_meanings={self.label_meanings}")

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, idx):
        card = self.cards[idx]
        pil = PIL.Image.open(os.path.join(self.dir, card))  # .convert("RGB")

        data = self.to_tensor(pil)
        label = torch.Tensor(self.labels.loc[card, :].values)

        sample = {
            "data": data,
            "label": label,
            "img_idx": idx,
        }
        print(f"get_item({card})")
        print(f"sample={sample}")
        return sample

    @classmethod
    def to_tensor(self, pil):
        ChosenTransforms = transforms.Compose(
            [
                transforms.PILToTensor(),
                transforms.ConvertImageDtype(torch.float),
            ]
        )
        return ChosenTransforms(pil)
