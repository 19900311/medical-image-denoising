import os
import numpy as np
import matplotlib.pyplot as plt

from pydicom import dcmread

from numpy import ndarray
from typing import NoReturn


def read_images(path: str) -> list[ndarray]:
    np_images = []
    for file in os.listdir(path):
        dcm_image = dcmread(os.path.join(path, file))
        np_images.append(dcm_image.pixel_array)

    return np_images


def plot_images(images: list[ndarray], figsize: tuple) -> NoReturn:
    dim = int(np.round(np.sqrt(len(images))))
    _, axes = plt.subplots(dim, dim, figsize=figsize)
    for image, axis in zip(images, axes.flatten()):
        axis.imshow(image, cmap="gray")

    plt.show()
