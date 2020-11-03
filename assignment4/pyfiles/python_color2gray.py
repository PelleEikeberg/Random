import cv2
from time import time


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


def generating_report_python(image_name, function, iterations=3, printing=True):
    """
    opens a reportfile and wrties the avarege runstime of python implementation of function ran over n-iterations.
    if printing == True, then it printsout also

    Parameters:
    ----------
        image_name (str): The file name or dir/name of an image file ex "rain.jpg"

        fuction (function): The function to use to return
            the image matrix ex: "open_image" or "python_color2gray"

        iterations (int): the numper of times to run the function over

        printing (bool): whether or not to print out some time info

    Returns:
    -------
        None: saves the file, does not return anything
    """
    image = open_image(image_name)

    str1 = "Timing: " + function.__name__ + "\n"
    str2 = (
        "Average runtime running "
        + str(function.__name__)
        + " after "
        + str(iterations)
        + " runs: "
    )
    str3 = "Timing preformed using: " + str(image.shape)

    sumtime = 0
    for i in range(iterations):
        startclock = time()
        function(image)
        stopclock = time()
        difftime = stopclock - startclock
        sumtime += difftime
        if printing:
            print("time running nr: ", i + 1, " is :", difftime, " s")

    if printing:
        print(
            "\nAverage runtime running " + function.__name__ + " after ",
            iterations,
            " runs:\n",
            sumtime / iterations,
            "s",
        )
        print("Timing performed using :\n", image.shape)

    str2 += str(sumtime / iterations) + " s\n"

    words = str(function.__name__).split("_")

    infile = open("../reports/" + words[0] + "_report_" + words[1] + ".txt", "w")

    for i in [str1, str2, str3]:
        infile.writelines(i)

    infile.close()


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
    image = cv2.imread("../images/" + str(name))
    # saves the image as array by Interpretatin it as RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def saving_image(image, fuction, name, image_format=".jpeg"):
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
    fname = fuction.__name__
    cv2.imwrite("../images/" + str(name) + "_" + fname + image_format, image)


if __name__ == "__main__":
    generating_report_python("rain.jpg", python_color2gray)
    saving_image(open_image("rain.jpg"), python_color2gray, "rain")
