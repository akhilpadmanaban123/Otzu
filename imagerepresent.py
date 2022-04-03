import cv2
from matplotlib import pyplot as plt
from findthreshold import otsu_implementation

def call_otsu_threshold(img_title="D:\palmleaf.jpg", is_reduced_noise=False):
    image=cv2.imread(img_title,0)

    #applying gaussian blur to reduce the noise
    if is_reduced_noise:
        image=cv2.GaussianBlur(image,(5,5),0)

    #view the initial image histogram
    plt.hist(image.ravel(),256)
    plt.xlabel('Color intensity')
    plt.ylabel('Number of pixels')
    plt.savefig('Image_hist.png')
    plt.show()
    plt.close()

    '''applying the otsu's method setting the flag value into 
        cv2.THRESH_OTSE.
            Use bmodal image as input
            Optimal threshold value is determined automatically'''

    otsu_threshold,image_result=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,)
    print('Obtained threshold: ',otsu_threshold)

    #view the reesulting histogram
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.hist(image_result.ravel(),256)
    ax.set_xlabel('Color intesity')
    ax.set_ylabel('Number of pixels')
    ###
    plt.savefig('Image_hist_result.png')
    plt.close()

    #visualizing thhe image after Otsu's method application
    cv2.imshow("Otsu's thresholding result =",image_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    call_otsu_threshold()
    otsu_implementation

if __name__=="__main__":
    main()
