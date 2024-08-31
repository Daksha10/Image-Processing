import cv2
import numpy as np
import matplotlib.pyplot as plt


def edgedetection():
    # read the image
    image = cv2.imread("beetle.jpg")
    # convert it to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #show the grayscale image
    plt.imshow(gray, cmap="gray")
    plt.show()
    # performing the canny edge detector to detect image edges
    edges = cv2.Canny(gray,30,100)
    plt.imshow(edges)
    plt.show()

def cartoon():
    # Load the image using cv2
    img = cv2.imread("download.jpg")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #Convert to grayscale and apply median blur to reduce image noise
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.medianBlur(grayimg, 5)

    #Get the edges 
    edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    #Convert to a cartoon version
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    #Display original image
    plt.figure()
    plt.imshow(img)
    plt.axis("off")
    plt.title("Original Image")
    plt.show()

    #Display cartoon image
    plt.figure()
    plt.imshow(cartoon)
    plt.axis("off")
    plt.title("Cartoon Image")
    plt.show()

def contours():
    #loading a simple image 
    image = cv2.imread('star.jpg')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edges = cv2.Canny(gray, 30, 200)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Finding Contours
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('Canny Edges After Contouring', edges)
    cv2.waitKey(0)

    print("Number of Contours found = " + str(len(contours)))

    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pencil_sketch():
    img=cv2.imread("anne.jpg")
    cv2.imshow("original image",img)
    plt.imshow(img)
    plt.axis(False)
    plt.show()
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(RGB_img)
    plt.axis(False)
    plt.show()
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    
    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    cv2.imwrite('sketch.png', sketch_img)
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(RGB_img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title('Sketch', size=18)
    rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()
    


def main():
    """print("MENU:")
    print("1.Edge detection.")
    print("2.Image to Cartoon.")
    print("3.Finding Contours.")
    print("4.Pencil Sketch.")
    choice=int(input("Enter your choice from the above:"))"""
    choice = 1
    while (choice!=5):
        print("MENU:")
        print("1.Edge detection.")
        print("2.Image to Cartoon.")
        print("3.Finding Contours.")
        print("4.Pencil Sketch.")
        print("5.Exit.")
        choice = int(input("Enter your choice from the above: "))
        if choice==1:
            edgedetection()
        elif choice==2:
            cartoon()
        elif choice==3:
            contours()
        elif choice==4:
            pencil_sketch()
        elif choice==5:
            pass
        else:
            print("Enter valid Choice!!")
main()
