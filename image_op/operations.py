import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        
        # add your code here
        # Create a blank image for merge
        mergedImage = np.zeros([len(image_left), len(image_left[0]), 3])
        # print (mergedImage)
        # Fill left of new image from the input left image
        for i in range(len(mergedImage)):
            for j in range(0, column):
                mergedImage[i][j] = image_left[i][j]

        # Fill right of new image from the input right image
        for i in range(len(mergedImage)):
            for j in range(column, len(mergedImage[i])):
                mergedImage[i][j] = image_right[i][j]

        # Please do not change the structure
        return mergedImage  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, output_image, column, alpha, beta):
# print (output_image)


        """
        Scale your image intensity.

        output_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        # Scale intensity for left image by alpha
        for i in range(len(output_image)):
            for j in range(0, column):
                output_image[i][j] = output_image[i][j]*alpha

        # Scale intensity for right image by beta
        for i in range(len(output_image)):
            for j in range(column, len(output_image[i])):
                output_image[i][j] = output_image[i][j]*beta

        # Please do not change the structure
        return output_image

    def centralize_pixel(self, output_image, column):

        """
        Centralize your pixels (do not use np.mean)

        output_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here
        ml = 0
        leftpixelcount = 0
        rl = 0
        rightpixelcount = 0

        # Get total intensity of left image
        for i in range(len(output_image)):
            for j in range(0, column):
                ml += output_image[i][j]
                leftpixelcount += 1

        # Get total intensity of right image
        for i in range(len(output_image)):
            for j in range(column, len(output_image[i])):
                rl += output_image[i][j]
                rightpixelcount += 1

        # Compute Avergages
        ml /= leftpixelcount
        rl /= rightpixelcount
        # Compute Offsets
        Ol = 128 - ml
        Or = 128 - rl

        # Apply Offsets
        for i in range(len(output_image)):
            for j in range(0, column):
                output_image[i][j] += Ol
        for i in range(len(output_image)):
            for j in range(column, len(output_image[i])):
                output_image[i][j] += Or

        return output_image
