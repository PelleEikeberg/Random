# Assignment 4

This assignment is about python code optimization, image manipulation, and package usage in python.

  - python -> numpy -> numba -> (cython optional)
  - How image malipulation works
  - package usage 

### Folder structure:

| Folder | Inside |
| ------ | ------ |
| instapy | the entirity of the package instapy |
| pyfiles | the python/numpy/numba _color2gray.py and _color2sepia.py files|
| images | "rain.jpg" and all other malipulated versions |
| reports | auto generated reports showing timing and comparisons |



## Instapy:
The python package that conatains all of the functionality and more of the files in [pyfiles](https://github.uio.no/IN3110/IN3110-pellee/tree/master/assignment4/pyfiles). The added functionality includes: excecutable file in /bin/. when installing via "pip install ." you also get "instapy" as a terminal function. 

### How to install:
```
cd Where_You_Have_Cloned_The_Repo/assignment4/instapy/
pip install .
...
```
Then run
```
instapy -f ../images/rain.jpg -o ../out.jpg -g
```
this should work. now you can call instapy from anywhere in the terminal. when using images. include the entire path from where you are, or have the image in the same folder as you are in.
if encauntering some problem. the "instapy -h" or "instapy --help" might come in handy.

### Using instapy as import:
The terminal function is usefull, and in most cases this might be the fastest option. If you are working with images in python, and want to apply the sepia or gray filter, then you can slo import it!

When in a python program you can use instapy like this (the python program can be anywhere in the file struckture)
```py
import instapy as inp
inp.grayscale_image("rain.jpg","gray_rain.jpg")
```
or
```py
from instapy import grayscale_image
grayscale_image("rain.jpg","gray_rain.jpg")
```
you can even do:
```py
import instapy
instapy.instapy.grayscale_image("rain.jpg","gray_rain.jpg")
```
This is because the package instapy contains the instapy.py file, which has the functions. the functions are automaticly imported and can thus be used by only importing the package. but you can also import the function from the instapy.py file and then do something with it.



## Pyfiles:
##### python_color2gray.py

This is mostly to show how to open and malipulate an image. also to be of comparison to the other solutions. More indepth explanation in the [pyfiles](https://github.uio.no/IN3110/IN3110-pellee/tree/master/assignment4/pyfiles) folder. 

##### numpy_color2gray.py
This is to show off how numpy works by not needing for-loops. after showing off how slicing will improve the timing. the README file in [pyfiles](https://github.uio.no/IN3110/IN3110-pellee/tree/master/assignment4/pyfiles) folder goes more indepth about the pro´s and con´s of using numpy.

##### numba_color2gray.py
This is to show how if you exclude numy but compile python code with c++ you can achieve faster times than even numpy. the drawback is the compilation time, and unless you should need the code to run on repeate many times it might be worth it to run numpy instead. More inside [pyfiles](https://github.uio.no/IN3110/IN3110-pellee/tree/master/assignment4/pyfiles) folder.

##### python/numpy/numba _color2gray.py
This is just to add to more things to do with the image for when we make a prackage. the pro´s and con´s for the different methods still applies, but are more obvious now.

## Images:
In this assignment, we are going to manipulate the "rain.jpg" image. (the code will still apply for all images)



![alt text](https://raw.githubusercontent.com/PelleEikeberg/Random/master/assignment4/images/rain.jpg)

The first part is to apply a grayscale to the image. We have been given the math-formula so we only need to apply it. After each pixel has been given the same value we can be shure it will be in the range white->black.



![alt text](https://raw.githubusercontent.com/PelleEikeberg/Random/master/assignment4/images/RGB_to_gray_explanation.jpeg)

After applying we get:



![alt text](https://raw.githubusercontent.com/PelleEikeberg/Random/master/assignment4/images/rain_python_color2gray.jpeg)



The sepia is the same prisiple except we have different weights for the different pixels. the result is:



![alt text](https://raw.githubusercontent.com/PelleEikeberg/Random/master/assignment4/images/rain_python_color2sepia.jpeg)


## Reports:
The report files are used to compare the times the different scripts use to run. For the python_color2(gray/sepia).txt the time for the scripts average over n runs (here n=3). For all other reports the methods that came before is also chacked the avarage time against.
for numpy_report_color2gray.txt:
```
Timing: numpy_color2gray
Average runtime running numpy_color2gray after 3 runs: 0.0032805601755777993 s
Average runtime running of numpy_color2gray is 550.8963637685022 times faster than python_report_color2gray.txt
Timing preformed using: (400, 600, 3)
```
The average time for the script "numpy_color2gray.py" is timed over n=3 times. and it compares (from python_report_color2gray.txt) how many times faster this version is. 
the last info is about the image file size. (H,W,C). 
H = height
W = width
C = colors (3 = RBG)


