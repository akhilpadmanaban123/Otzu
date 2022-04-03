''''
Otzu threshold detecting algorithm,
Calling this package can detect the threshold value based on the
image
'''


import cv2
import numpy as np


def otsu_implementation(img_title="D:\palmleaf.jpg", is_normalized=False, is_reduced_noise=False):
    image = cv2.imread(img_title, 0)

    # applying gaussian blur to reduce the image blurness
    if is_reduced_noise:
        image = cv2.GaussianBlur(image, (5, 5), 0)


    bins_nums=256  #setting total number of bins in histogram

    #getting the image histogram
    hist, bins_edges = np.histogram(image, bins=bins_nums)

    #getting normalized histogram if needed
    if is_normalized:
        hist=np.divide(hist.ravel(),hist.max())

    #calculate the center of bins
    bin_mids=(bins_edges[:-1]+bins_edges[1:])/2

    #getting the probabilities of w1(t),w2(t)  ( Iteratinf over all the thresholds)
    weight1=np.cumsum(hist)
    weight2=np.cumsum(hist[::-1])[::-1]

    #getting the class mean mu0(t)
    mean1=np.cumsum(hist*bin_mids)/weight1
    #getting the class mean mu1(t)
    mean2=(np.cumsum((hist*bin_mids)[::-1])/ weight2[::-1])[::-1]

    inter_class_variance=weight1[:-1]*weight2[1:]* (mean1[:-1]-mean2[1:])**2

    #maximize the inter_class_variance function value
    index_of_max_value=np.argmax(inter_class_variance)

    threshold=bin_mids[:-1][index_of_max_value]

    print("Otzu's algorithm implementation threshold value",threshold)
    return threshold


def main():
    otsu_implementation()


if __name__ == "__main__":
    main()
