import cv2
from time import time
from numba import jit
from python_color2gray import open_image, saving_image
from numba_color2gray import generating_report_numba


@jit(nopython=True)
def numba_color2sepia(image):
    """
    Uses numba to go through each element in image matrix and then set the sepia.

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
    weights = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]

    # finds the max in weigth sum to stop overflow.
    """The sum of an individual correction in the weights will be over 1, so we corrigate by
    mulitplying with the highest sum divided buy 1. this results in the highest RGB beeing 255 and
    not higher.
    """
    W = 1
    for weg in weights:
        if W < (weg[0] + weg[1] + weg[2]):
            W = weg[0] + weg[1] + weg[2]

    # when we set the values outside the for loop it runs faster.
    # this only help when running numba that improves when it does not have to
    # set variable types to often
    RW0, RW1, RW2 = weights[2][-1], weights[2][-2], weights[2][-3]
    GW0, GW1, GW2 = weights[1][-1], weights[1][-2], weights[1][-3]
    BW0, BW1, BW2 = weights[0][-1], weights[0][-2], weights[0][-3]

    # loops through H array
    for i in range(len(image)):
        # loops through W array
        for j in range(len(image[i])):
            # applies the filter
            rsepia = (
                (image[i, j, 0] * RW0 + image[i, j, 1] * RW1 + image[i, j, 2] * RW2)
                * 1
                / W
            )
            gsepia = (
                (image[i, j, 0] * GW0 + image[i, j, 1] * GW1 + image[i, j, 2] * GW2)
                * 1
                / W
            )
            bsepia = (
                (image[i, j, 0] * BW0 + image[i, j, 1] * BW1 + image[i, j, 2] * BW2)
                * 1
                / W
            )

            # sets the new image values
            image[i, j] = rsepia, gsepia, bsepia

    return image


if __name__ == "__main__":
    generating_report_numba("rain.jpg", numba_color2sepia)
    saving_image(open_image("rain.jpg"), numba_color2sepia, "rain")
