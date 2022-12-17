import os

import pandas as pd

from PIL import Image, ImageOps
from PIL.JpegImagePlugin import JpegImageFile


def print_stats():
    """explore dataset"""
    path = os.path.join(os.getcwd(), "img")
    data = []
    for f in os.listdir(path):
        img = Image.open(os.path.join(path, f))
        data.append([f, img.width, img.height])
    df = pd.DataFrame(data, columns=["Image", "Width", "Height"])
    print(f"range W = {df['Width'].min()} - {df['Width'].max()}")
    print(f"range H = {df['Height'].min()} - {df['Height'].max()}")
    print(f"avg W, H = {int(df['Width'].mean())}, {int(df['Height'].mean())}")


HEIGHT = 570  # min height in dataset
WIDTH = 1008  # min width in dataset


def resize(img: JpegImageFile):
    """resize to the larger of the 2 minimum dimentions, shrink to fit"""
    if img.width >= WIDTH:
        pw = (img.width - WIDTH) / img.width
        h = img.height - (img.height * pw)
    if img.height >= HEIGHT:
        ph = (img.height - HEIGHT) / img.height
        w = img.width - (img.width * ph)
    if h - HEIGHT < 0:
        img = img.resize((int(w), HEIGHT))
    elif w - WIDTH < 0:
        img = img.resize((WIDTH, int(h)))
    else:
        raise Exception(f"Error with resize: {w} {h} {img}")
    return img


def crop(img: JpegImageFile):
    """crop after resize to normalize size"""
    if img.height > HEIGHT:
        img = img.crop((0, 0, img.width, HEIGHT))
    if img.width > WIDTH:
        img = img.crop((0, 0, WIDTH, img.height))
    return img


def grey(img: JpegImageFile):
    return ImageOps.grayscale(img)


def normalize(img: JpegImageFile) -> None:
    """in order"""
    img = resize(img)
    img = crop(img)
    img = grey(img)
    return img


def normalize_all():
    path_in = os.path.join(os.getcwd(), "img")
    path_out = os.path.join(os.getcwd(), "norm")
    for f in os.listdir(path_in):
        img = Image.open(os.path.join(path_in, f))
        img = normalize(img)
        img.save(os.path.join(path_out, f))


if __name__ == "__main__":
    print_stats()
