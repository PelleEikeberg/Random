import cv2
import numpy as np
from time import time
from python_color2gray import open_image, saving_image
from numpy_color2gray import generating_report_numpy


# the main function
def numpy_color2sepia(image):
    """
    uses numpy slicing to go though each element in an image matrix and set the sepia

    Parameters:
    ----------
        image (<class 'numpy.ndarray'>):
            the image matrix of shape (H,W,3)

    Returns:
    -------
        image (<class 'numpy.ndarray'>):
            the sepia image matrix of shape (H,W,3)
    """

    # the weights for sepia given
    W = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
    S0 = np.sum(W[0])
    S1 = np.sum(W[1])
    S2 = np.sum(W[2])
    Scale = max([S0, S1, S2])
    Scale = 1 / Scale

    R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    # sets the grayscale
    Rs = (W[2, -1] * R + W[2, -2] * G + W[2, -3] * B) * Scale
    Gs = (W[1, -1] * R + W[1, -2] * G + W[1, -3] * B) * Scale
    Bs = (W[0, -1] * R + W[0, -2] * G + W[0, -3] * B) * Scale
    # sets the new RGB values.
    image[:, :, 0] = Rs
    image[:, :, 1] = Gs
    image[:, :, 2] = Bs

    return image


if __name__ == "__main__":
    generating_report_numpy("rain.jpg", numpy_color2sepia)
    saving_image(open_image("rain.jpg"), numpy_color2sepia, "rain")
