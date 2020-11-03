
### The Instapy package

The instalation guide of the package is in the main README also.
The package includes all of the programs worked on this assignment

#### to install:
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

#### Using instapy as import:
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


## Testing:

the tesing file is only installed and not run. to test please use "pytest" in the instapy folder.

```
> pytest
...
> ============================== 3 passed in 1.97s ===============================
```
