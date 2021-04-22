# Digital Image Processing 
## Assignment - 0 ##

Due: Tue 09/15/20 11:59 PM

**1.  Image Merging:**

(5 pts.) Write a code to merge two images of the computer scientist *Grace Hopper*. In 1952, *Grace Hopper* and her team created the first compiler for computer languages.

![image_test2](https://user-images.githubusercontent.com/25855062/91643178-9f2d6380-e9f6-11ea-8cea-2313e80365c6.jpg)


The inputs to your function are: (i) image left: grace_1.png (size: 350Rows X 340Cols), (ii) image right: grace_2.png (size: 350R X 340C), (iii) image column (c) at which the images should be merged.

  - image_op/operations.py: Edit the function merge
    - Define a new image J as follows: the first c columns (default value = 155) should be equal to the left half of the (grace_1.png) image. The right section (340 - c)
    columns should be equal to the right section of the second (grace_2.png) image.
    
**2.  Intensity Scaling:**

(5 pts.) Write a code to scale the intensity of the left half of the merged image by scaling factor of alpha and the right half by a scaling factor of beta. 

*Image Scaling*: Image/Intensity scaling is a linear image operation where each pixel is multiplied by a scaling factor. The scaling factor is a value between 0 and 1.  
The inputs to your function are: (i) input image, (ii) image column at which left section ends, (iii) alpha: scaling factor for the left section (0 <= alpha <= 1) and (iv) beta: scaling factor for the right section ((0 <= beta <= 1).

  - image_op/operations.py: Edit the function intensity_scaling.
  
**3.  Centralizing pixel intensities:**

(5 pts.) Write a code to centralize the intensities of the two sections of the image.

Centralizing Pixels: When merging, the two images can have very different overall brightness values. Here the goal is to make sure that the average intensities of the left section and the right section are equal and cetralized (= 128).
After centralizing pixels, the average of all the pixels in the left section will be 128 and the average of all the pixels in the right section will be 128 as well.

Let M be the input image. Let l be all the intensities in left section of the image and r all the intensities in the right section of the image.

Steps:
1. Compute average intensity of left pixels. (m<sub>l</sub>)
2. Compute offset. (o<sub>l</sub> = 128 - m<sub>l</sub>)
3. For each pixel M<sub>l</sub>(x,y) in the left section add the offset. (M<sub>l</sub>(x,y) + o<sub>l</sub>)  
4. Compute average intensity of right pixels. (m<sub>r</sub>)
5. Compute offset. (o<sub>r</sub> = 128 - m<sub>r</sub>)
6. For each pixel M<sub>r</sub>(x,y) in the right section add the offset. (M<sub>r</sub>(x,y) + o<sub>r</sub>)

Note: After applying the operation, some pixels may endup being **< 0** or **> 255**. Clip these pixels, such that any value greater than 255 is assigned a value of 255, and any value less than zero will be assigned a value of 0.

The inputs to your function are: (i) image, (ii) image column at which left section ends.

  - image_op/operations.py: Edit the function centralize_pixel.
    - Do not use np.mean to compute the averages.
    
   
   
**Note:**

Do not use any in-built functions from opencv and numpy (E.g: np.mean). In general, you can use function from math library. <br/>
**Only Functions allowed** for this part are: np.array(), np.matrix(), np.zeros(), np.ones(), cv2.imread(), cv2.namedWindow(), cv2.waitKey().
   
  - Please do not change the code structure
  - Usage:
   
        - python dip_hw0.py -ir <image-name> -il <image2-name> -c <c> -a <alpha> -b <beta>
        - Example: python dip_hw0.py -il grace1.PNG -ir grace2.PNG -c 155
  - Please make sure the code runs when you run the above command from prompt/terminal
  - All the output images and files are saved to "output/" folder

Two images are provided for testing: grace_1.jpg and grace_2.png
  
PS. Please do not change: dip_hw0.py, requirements.txt, and Jenkinsfile. 


1. Operation      - 15 Pts.

    Total         - 15 Pts.


-----------------------

