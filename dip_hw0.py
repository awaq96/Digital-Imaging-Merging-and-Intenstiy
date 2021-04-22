"""dip_hw0.py: Starter file to run howework 0"""

__author__      = "Khadija Khaldi"
# revised by Zhenggang Li
__email__ = "kkhaldi@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
from datetime import datetime
from image_op import operations


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-il", "--image-left", dest="image_l",
                        help="specify the name of the left image", metavar="IMAGELEFT")
    parser.add_argument("-ir", "--image-right", dest="image_r",
                        help="specify the name of the right image", metavar="IMAGERIGHT")

    parser.add_argument("-c", "--column", dest="column",
                        help="specify column (c) for merging", metavar="COLUMN")

    parser.add_argument("-a", "--alpha", dest="alpha",
                        help="specify scaling factor for the left section of the image", metavar="ALPHA")
    parser.add_argument("-b", "--beta", dest="beta",
                        help="specify scaling factor for the right section of the image", metavar="BETA")

    args = parser.parse_args()

    # Load image
    if args.image_l is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_l = cv2.imread(args.image_l, 0)

    if args.image_r is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_r = cv2.imread(args.image_r, 0)

    # Check the location to merge
    if args.column is None:
        print("Merging location Y is not specified using default (155)")
        print("use the -h option to see usage information")
        column = 155
    else:
        column = int(args.column)
        if not column in range(0, input_image_l.shape[1]):
            print("column value ouside image bounds, value should be between 0 and %s" % (input_image_l.shape[1]))
            print("Using default value (160)")
            column = 155

    # Check the alpha is between 0 to 1
    if args.alpha is None:
        print('ALPHA not specified using default (1)')
        alpha = 1
    else:
        alpha = float(args.alpha)
        if alpha < 0 and alpha > 1:
            print("Alpha value should be between 0 and 1")
            print("Using default value (0.5)")
            alpha = 0.5

    if args.beta is None:
        print('BETA not specified using default (1)')
        beta = 1
    else:
        beta = float(args.beta)
        if beta < 0 and beta > 1:
            print("Beta value should be between 0 and 1")
            print("Using default value (0.5)")
            beta = 0.5

    # Write output file
    outputDir = 'output/'
    operation_obj = operations.Operation()

    merged_image = operation_obj.merge(input_image_l, input_image_r, column=column)
    output_image_name = outputDir + 'merged_image' + ".jpg"
    cv2.imwrite(output_image_name, merged_image)

    scaled_image =operation_obj.intensity_scaling(merged_image, column=column, alpha=alpha, beta=beta)
    output_image_name = outputDir + 'scaled_image' + ".jpg"
    cv2.imwrite(output_image_name, scaled_image)

    centralized_pixels = operation_obj.centralize_pixel(merged_image, column=column)
    output_image_name = outputDir + 'centralized_image' + ".jpg"
    cv2.imwrite(output_image_name, centralized_pixels)


if __name__ == "__main__":
    main()







