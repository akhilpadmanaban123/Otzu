# Otzu
Otzu global thresholding ( Image binarization for palm leaf basic demo)
Image Thresholding- (Preprocessing step)
	Binarizing the image based on the pixel intensities.
	Input is : Grayscale and a threshold image
	Output is : Binary image
If the intensity of the input image is greater than the threshold, then the  output pixel is marked as white.  If the intensity of the image is lesser than the threshold, then the output pixel is marked as black.

Otzu Thresholding automatically determines the threshold value needed for the binarization, whereas in other simpler Thresholdings, we have to manually specify the threshold value
—--------------------------------------------------------------------------
Image Segmentation
	A class of algorithms which partitions the images into different segments or groups based on pixels.

   Image Thresholding is the simplest kind of image segmentation,  it partitions the image into 2 group of pixels, white for foreground and black for background.
Divided into two  —--- Local Thresholding and Global Thersholding.
	In Global Thresholding, a single threshold value is used globally for the whole image.
	In Local Thresholding, different threshold value is used globally for the image. Based on some characteristics of the soms area of the images.
—---------------------------------------------------
OTZU Global Thresholding

Otzu thresholding is applied to images which are bi-model (Images with 2 peaks in the histogram).
Process the input image
Obtain image histogram (distribution of pixels)
Compute the threshold value 
Replace image pixels into white in those regions, where saturation is greater than  and into the black in the opposite cases.
Implementation
Read the image, Apply gaussian blurriness to reduce the noise from the image
Calculate the Orsu’s threshold
 
—--------------------------------------------------------------
