import cv2
from time import time
from python_color2gray import open_image, saving_image, generating_report_python

# the main function
def python_color2sepia(image):
    """
    The python way to loop over each H and W of an imgae and set the sepia to each pixel.

    Parameters:
    ----------
        image (<class 'numpy.ndarray'>):
            the image matrix of shape (H,W,3)

    Returns:
    -------
        image (<class 'numpy.ndarray'>):
            the gray image matrix of shape (H,W,3)
    """
    W = 1

    # the weights for sepia given
    weights = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]

    # finds the max in weigth sum to stop overflow.
    """The sum of an individual correction in the weights will be over 1, so we corrigate by
    mulitplying with the highest sum divided buy 1. this results in the highest RGB beeing 255 and
    not higher.
    """
    for i in weights:
        if W < sum(i):
            W = sum(i)
    # loops through H array
    for i in range(len(image)):
        # loops through W array
        for j in range(len(image[i])):

            # applies the filter
            rsepia = (
                (
                    image[i, j, 0] * weights[2][-1]
                    + image[i, j, 1] * weights[2][-2]
                    + image[i, j, 2] * weights[2][-3]
                )
                * 1
                / W
            )
            gsepia = (
                (
                    image[i, j, 0] * weights[1][-1]
                    + image[i, j, 1] * weights[1][-2]
                    + image[i, j, 2] * weights[1][-3]
                )
                * 1
                / W
            )
            bsepia = (
                (
                    image[i, j, 0] * weights[0][-1]
                    + image[i, j, 1] * weights[0][-2]
                    + image[i, j, 2] * weights[0][-3]
                )
                * 1
                / W
            )

            # sets the new image values
            image[i, j] = rsepia, gsepia, bsepia

    return image


if __name__ == "__main__":
    generating_report_python("rain.jpg", python_color2sepia)
    saving_image(open_image("rain.jpg"), python_color2sepia, "rain")
