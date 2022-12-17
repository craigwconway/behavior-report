import os


def rename_images(img_dir="img/"):
    for i, file in enumerate(os.listdir(dir)):
        if os.path.isfile(dir + file):
            print(f"renaming {file} to {i}.png")
            os.rename(dir + file, dir + f"{i}.png")
    print(f"Done")
