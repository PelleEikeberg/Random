import cv2
import numpy as np
from time import time
from python_color2gray import open_image, saving_image


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


def generating_report_numpy(image_name, function, iterations=3, printing=True):
    """
    opens a reportfile and wrties the avarege runstime of numpy implementation of function ran over n-iterations.
    if printing == True, then it printsout also. it aslo opens the python report and compares the run times.

    Parameters:
    ----------
        image_name (str): The file name or dir/name of an image file ex "rain.jpg"

        fuction (function): The function to use to return
            the image matrix ex: "open_image" or "numpy_color2gray"

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
    str3 = "Average runtime running of " + str(function.__name__) + " is "
    str4 = "Timing preformed using: " + str(image.shape)

    ending = "_" + function.__name__.split("_")[-1]

    sumtime = 0
    for i in range(iterations):
        startclock = time()
        function(image)
        stopclock = time()
        difftime = stopclock - startclock
        sumtime += difftime
        if printing:
            print("time running nr: ", i + 1, " is :", difftime, " s")

    avgtime = sumtime / iterations

    if printing:
        print(
            "\nAverage runtime running " + function.__name__ + " after ",
            iterations,
            " runs:\n",
            avgtime,
            "s",
        )
        print("Timing performed using :\n", image.shape)

    str2 += str(avgtime) + " s\n"

    def reading_report(name):
        infile = open("../reports/" + str(name) + "_report" + ending + ".txt", "r")
        infile.readline()
        words = infile.readline().split(" ")
        avgtime = words[-2]
        return float(avgtime)

    pythontime = reading_report("python")

    if pythontime > avgtime:
        str3 += (
            str(pythontime / avgtime)
            + " times faster than "
            + "python"
            + "_report"
            + ending
            + ".txt\n"
        )
    if avgtime > pythontime:
        str3 += (
            str(avgtime / pythontime)
            + " times slower than "
            + "python"
            + "_report"
            + ending
            + ".txt\n"
        )

    words = str(function.__name__).split("_")

    infile = open("../reports/" + words[0] + "_report_" + words[1] + ".txt", "w")

    for i in [str1, str2, str3, str4]:
        infile.writelines(i)

    infile.close()


if __name__ == "__main__":
    generating_report_numpy("rain.jpg", numpy_color2gray)
    saving_image(open_image("rain.jpg"), numpy_color2gray, "rain")
