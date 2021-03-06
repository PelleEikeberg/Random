#!/usr/bin/env python3
import cv2
import numpy as np
from numba import jit
import argparse


def grayscale_image(
    input_filename, output_filename=None, implementation="numpy", scale=100
):
    """
    A function that can turn an image from RGB to grayscale. The input_filename has to be entered and will be used to open the file
    the output_filename is only used if the user wants to save the resulting image. the implementation is numpy by default, since this is
    the fastest solution, but other solutions can be choosen. scale is used to down/up -scale the image.

    Parameters:
    ----------
        input_filename (str): a filename or dst/filename of the file to be opened

        output_filename (str): the output filename or dst/filename or the grayscale file

        impementation (str): the implementation to be used (numpy/python/numba)

        scale (int): the scale factor written in precent

    Returns:
    -------
        image (<class 'numpy.ndarray'>):
            the image matrix of shape (H,W,3)


    """

    def rescale(image, scale_percent):
        """
        Rescales the image to the percent scale given.

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

            scale (int): the scale factor written in precent

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H*scale,W*scale,3)
        """
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        output = cv2.resize(image, dsize)

        return output

    def open_image(name):
        """
        Opens the image and returns the image matrix for that file

        Parameters:
        ----------
            image (str):
                the image name of file: ex: "rain.jpg" or "images/rain.jpg"

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)
        """
        # open the image file
        image = cv2.imread(str(name))
        # saves the image as array by Interpretatin it as RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def saving_image(image, fuction, name):
        """
        Saving the image matrix of a function output to a filename

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

            fuction (function): The function to use to return
                the image matrix ex: "open_image" or "python_color2gray"

            name (str): the file or dir/file of the file to be saved. ex: "images/rain.jpg"

        Returns:
        -------
            None: saves the file, does not return anything
        """
        image = fuction(image).astype("uint8")
        cv2.imwrite(name, image)

    def python_color2gray(image):
        """
        The python way to loop over each H and W of an imgae and set the grayscale to each pixel.

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the gray image matrix of shape (H,W,3)
        """
        # the grayscale weights given from the task
        weights = [0.21, 0.72, 0.07]

        # runs through the height dimentions
        for i in range(len(image)):
            # runs throguh the width dimentions
            for j in range(len(image[i])):
                # applies the grayscale by summing of the channels and multiplying it with the respective weight
                graysum = (
                    image[i, j, 0] * weights[-1]
                    + image[i, j, 1] * weights[-2]
                    + image[i, j, 2] * weights[-3]
                )
                # updates the pixels with the gray value. all pixels have to be save value.
                image[i, j] = graysum, graysum, graysum

        return image

    def numpy_color2gray(image):
        """
        uses numpy slicing to go though each element in an image matrix and set the grayscale

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the gray image matrix of shape (H,W,3)
        """

        # pulls out the RGB values.
        rval, gval, bval = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        # sets the grayscale
        weighted = 0.07 * rval + 0.72 * gval + 0.21 * bval
        # sets the new RGB values.
        image[:, :, 0] = weighted
        image[:, :, 1] = weighted
        image[:, :, 2] = weighted

        return image

    @jit(nopython=True)
    def numba_color2gray(image):
        """
        Uses numba to go through each element in image matrix and then set the grayscale.

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the gray image matrix of shape (H,W,3)
        """
        weights = [0.21, 0.72, 0.07]
        w0 = weights[-1]
        w1 = weights[-2]
        w2 = weights[-3]

        for i in range(len(image)):
            for j in range(len(image[i])):
                graysum = (
                    image[i, j, 0] * w0 + image[i, j, 1] * w1 + image[i, j, 2] * w2
                )
                image[i, j] = graysum, graysum, graysum

        return image

    if output_filename != None:
        saving_image(
            rescale(open_image(input_filename), scale),
            eval(str(implementation) + "_color2gray"),
            output_filename,
        )

    if type(input_filename) != str:
        return eval(str(implementation) + "_color2gray")(input_filename)
    else:
        return eval(str(implementation) + "_color2gray")(
            rescale(open_image(input_filename), scale)
        )


def sepia_image(
    input_filename, output_filename=None, implementation="numpy", scale=100
):
    """
    A function that can turn an image from RGB to sepia. The input_filename has to be entered and will be used to open the file
    the output_filename is only used if the user wants to save the resulting image. the implementation is numpy by default, since this is
    the fastest solution, but other solutions can be choosen. scale is used to down/up -scale the image.

    Parameters:
    ----------
        input_filename (str): a filename or dst/filename of the file to be opened

        output_filename (str): the output filename or dst/filename or the sepia file

        impementation (str): the implementation to be used (numpy/python/numba)

        scale (int): the scale factor written in precent

    Returns:
    -------
        image (<class 'numpy.ndarray'>):
            the image matrix of shape (H,W,3)

    """

    def rescale(image, scale_percent):
        """
        Rescales the image to the percent scale given.

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

            scale (int): the scale factor written in precent

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H*scale,W*scale,3)
        """
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        output = cv2.resize(image, dsize)

        return output

    def open_image(name):
        """
        Opens the image and returns the image matrix for that file

        Parameters:
        ----------
            image (str):
                the image name of file: ex: "rain.jpg" or "images/rain.jpg"

        Returns:
        -------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)
        """
        # open the image file
        image = cv2.imread(str(name))
        # saves the image as array by Interpretatin it as RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def saving_image(image, fuction, name):
        """
        Saving the image matrix of a function output to a filename

        Parameters:
        ----------
            image (<class 'numpy.ndarray'>):
                the image matrix of shape (H,W,3)

            fuction (function): The function to use to return
                the image matrix ex: "open_image" or "python_color2gray"

            name (str): the file or dir/file of the file to be saved. ex: "images/rain.jpg"

        Returns:
        -------
            None: saves the file, does not return anything
        """
        image = fuction(image).astype("uint8")
        cv2.imwrite(name, image)

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
                the sepia image matrix of shape (H,W,3)
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
        W = np.array(
            [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
        )
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

    if output_filename != None:
        saving_image(
            rescale(open_image(input_filename), scale),
            eval(str(implementation) + "_color2sepia"),
            output_filename,
        )

    if type(input_filename) != str:
        return eval(str(implementation) + "_color2sepia")(input_filename)
    else:
        return eval(str(implementation) + "_color2sepia")(
            rescale(open_image(input_filename), scale)
        )
