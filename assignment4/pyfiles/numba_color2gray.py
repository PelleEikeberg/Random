import cv2
from time import time
from numba import jit
from python_color2gray import open_image, saving_image


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
            graysum = image[i, j, 0] * w0 + image[i, j, 1] * w1 + image[i, j, 2] * w2
            image[i, j] = graysum, graysum, graysum

    return image


def generating_report_numba(image_name, function, iterations=3, printing=True):
    """
    opens a reportfile and wrties the avarege runstime of numba implementation of function ran over n-iterations.
    if printing == True, then it printsout also. compares the python and numpy report times to the time run.

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
    str3 = "Average runtime running of " + str(function.__name__) + " is "
    str4 = "Average runtime running of " + str(function.__name__) + " is "
    str5 = "Timing preformed using: " + str(image.shape)

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
    numpytime = reading_report("numpy")

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

    if numpytime > avgtime:
        str4 += (
            str(numpytime / avgtime)
            + " times faster than "
            + "numpy"
            + "_report"
            + ending
            + ".txt\n"
        )
    if avgtime > numpytime:
        str4 += (
            str(avgtime / numpytime)
            + " times slower than "
            + "numpy"
            + "_report"
            + ending
            + ".txt\n"
        )

    words = str(function.__name__).split("_")

    infile = open("../reports/" + words[0] + "_report_" + words[1] + ".txt", "w")

    for i in [str1, str2, str3, str4, str5]:
        infile.writelines(i)

    infile.close()


if __name__ == "__main__":
    generating_report_numba("rain.jpg", numba_color2gray)
    saving_image(open_image("rain.jpg"), numba_color2gray, "rain")
