#!/usr/bin/env python3
import cv2
import numpy as np
from numba import jit
import argparse


def grayscale_image(input_filename, output_filename=None, implementation="numpy"):

    def open_image(name):
        #open the image file
        image = cv2.imread(str(name))
        #saves the image as array by Interpretatin it as RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def saving_image(image,fuction,name):
        image = fuction(image).astype("uint8")
        cv2.imwrite(name, image)
    

    def python_color2gray(image):
        """
        loops through all pixels of an image and apllies the weighted average to all of them
        saves all new pixels in the previous place. and return image array.

        input:
        -----
        image:  numpy.array     of shape: (x,y,3) where x is the height and y the width and 3 is RGB challens of the image


        output:
        -----
        image:  numpy.array     of shape: (x,y,3) where x is the height and y the width and 3 is RGB challens of the image
        """
        #the grayscale weights given from the task
        weights = [0.21,0.72,0.07]

        #runs through the height dimentions
        for i in range(len(image)):
            #runs throguh the width dimentions
            for j in range(len(image[i])):
                #applies the grayscale by summing of the channels and multiplying it with the respective weight
                graysum = image[i,j,0]*weights[-1] + image[i,j,1]*weights[-2] + image[i,j,2]*weights[-3]
                #updates the pixels with the gray value. all pixels have to be save value.
                image[i,j] = graysum, graysum, graysum

        return image

    def numpy_color2gray(image):

        #pulls out the RGB values.
        rval, gval, bval = image[:,:,0], image[:,:,1], image[:,:,2]
        #sets the grayscale
        weighted = 0.07*rval + 0.72*gval + 0.21*bval
        #sets the new RGB values.
        image[:,:,0] = weighted
        image[:,:,1] = weighted
        image[:,:,2] = weighted

        return image
    
    @jit(nopython=True)
    def numba_color2gray(image):
        """
        loops through all pixels of an image and apllies the weighted average to all of them
        saves all new pixels in the previous place. and return image array.

        input:
        -----
        image:  numpy.array


        output:
        -----
        image:  numpy.array
        """
        weights = [0.21,0.72,0.07]
        w0 = weights[-1]
        w1 = weights[-2]
        w2 = weights[-3]

        for i in range(len(image)):
            for j in range(len(image[i])):
                graysum = image[i,j,0]*w0 + image[i,j,1]*w1 + image[i,j,2]*w2
                image[i,j] = graysum, graysum, graysum

        
        return image

    if output_filename != None:
        try:
            saving_image(open_image(input_filename),eval(str(implementation)+"_color2gray"),output_filename)
        except:
            print("hei")
    

    if type(input_filename) != str:
        return eval(str(implementation)+"_color2gray")(input_filename)
    else:
        return eval(str(implementation)+"_color2gray")(open_image(input_filename))


def sepia_image(input_filename, output_filename=None, implementation="numpy"):

    def open_image(name):
        #open the image file
        image = cv2.imread(str(name))
        #saves the image as array by Interpretatin it as RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def saving_image(image,fuction,name):
        image = fuction(image).astype("uint8")
        cv2.imwrite(name, image)
    

    def python_color2sepia(image):
        """
        loops through all pixels of an image and apllies the weighted average to all of them
        saves all new pixels in the previous place. and return image array.

        input:
        -----
        image:  numpy.array


        output:
        -----
        image:  numpy.array
        """
        W = 1

        #the weights for sepia given
        weights =[[ 0.393, 0.769, 0.189], [ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]]
        
        #finds the max in weigth sum to stop overflow.
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

                #applies the filter
                rsepia = (image[i,j,0]*weights[2][-1] + image[i,j,1]*weights[2][-2] + image[i,j,2]*weights[2][-3])*1/W
                gsepia = (image[i,j,0]*weights[1][-1] + image[i,j,1]*weights[1][-2] + image[i,j,2]*weights[1][-3])*1/W
                bsepia = (image[i,j,0]*weights[0][-1] + image[i,j,1]*weights[0][-2] + image[i,j,2]*weights[0][-3])*1/W

                #sets the new image values
                image[i,j] = rsepia, gsepia, bsepia

        return image

    def numpy_color2sepia(image):
        """
        loops through all pixels of an image and apllies the weighted average to all of them
        saves all new pixels in the previous place. and return image array.

        input:
        -----
        image:  numpy.array

        output:
        -----
        image:  numpy.array
        """

        #the weights for sepia given
        W =np.array([[ 0.393, 0.769, 0.189], [ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]])
        S0 = np.sum(W[0]); S1 = np.sum(W[1]); S2 = np.sum(W[2])
        Scale = max([S0,S1,S2])
        Scale = 1/Scale

        R, G, B = image[:,:,0], image[:,:,1], image[:,:,2]
        #sets the grayscale
        Rs = (W[2,-1]*R + W[2,-2]*G + W[2,-3]*B)*Scale
        Gs = (W[1,-1]*R + W[1,-2]*G + W[1,-3]*B)*Scale
        Bs = (W[0,-1]*R + W[0,-2]*G + W[0,-3]*B)*Scale
        #sets the new RGB values.
        image[:,:,0] = Rs
        image[:,:,1] = Gs
        image[:,:,2] = Bs

        
        return image
        
    @jit(nopython=True)
    def numba_color2sepia(image):
        """
        loops through all pixels of an image and apllies the weighted average to all of them
        saves all new pixels in the previous place. and return image array.

        input:
        -----
        image:  numpy.array


        output:
        -----
        image:  numpy.array
        """
        

        #the weights for sepia given
        weights =[[ 0.393, 0.769, 0.189], [ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]]
        
        #finds the max in weigth sum to stop overflow.
        """The sum of an individual correction in the weights will be over 1, so we corrigate by
        mulitplying with the highest sum divided buy 1. this results in the highest RGB beeing 255 and
        not higher.
        """
        W = 1
        for weg in weights:
            if W < (weg[0] + weg[1] + weg[2]):
                W = weg[0] + weg[1] + weg[2]

        #when we set the values outside the for loop it runs faster.
        #this only help when running numba that improves when it does not have to
        # set variable types to often
        RW0, RW1, RW2 = weights[2][-1] , weights[2][-2] ,weights[2][-3]
        GW0, GW1, GW2 = weights[1][-1] , weights[1][-2] ,weights[1][-3]
        BW0, BW1, BW2 = weights[0][-1] , weights[0][-2] ,weights[0][-3]

        
        # loops through H array
        for i in range(len(image)):
            # loops through W array
            for j in range(len(image[i])):
                #applies the filter
                rsepia = (image[i,j,0]*RW0 + image[i,j,1]*RW1 + image[i,j,2]*RW2)*1/W
                gsepia = (image[i,j,0]*GW0 + image[i,j,1]*GW1 + image[i,j,2]*GW2)*1/W
                bsepia = (image[i,j,0]*BW0 + image[i,j,1]*BW1 + image[i,j,2]*BW2)*1/W

                #sets the new image values
                image[i,j] = rsepia, gsepia, bsepia

        return image

    if output_filename != None:
        try:
            saving_image(open_image(input_filename),eval(str(implementation)+"_color2sepia"),output_filename)
        except:
            print("hei")
    
    if type(input_filename) != str:
        return eval(str(implementation)+"_color2sepia")(input_filename)
    else:
        return eval(str(implementation)+"_color2sepia")(open_image(input_filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program to change color of an image")
    parser.add_argument("-f", "--filename", type=str, required=True, metavar="", help="the name of path+name of an image, needs file ending")
    parser.add_argument("-o", "--output", type=str, required=False, metavar="", help="the name of path+name of the output image, optional. needs file ending")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--grayscale", action="store_true", help="to turn an image gray")
    group.add_argument("-s", "--sepia", action="store_true", help="to turn an image sepia")
    args = parser.parse_args()

    if args.grayscale != None:
        grayscale_image(args.filename, args.output)
    elif args.sepia != None:
        sepia_image(args.filename, args.output)
    