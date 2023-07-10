#this project is not that goog, it only resize image and you have to write the image name and have it in same file as source code, if you resize same file then it will not create new file as the name is same


import cv2  #module that will help in image processing

#configurable parameters
imageName = input("Enter image name: ")
if imageName==
resize = int(input("resize percent: "))


destination = f"New_{imageName}"
image = cv2.imread(imageName)   #.imread function reads the image



#resize formulae
width = int(image.shape[1] * resize / 100)   #we write image[1] for width and image[0] for height
height = int(image.shape[0] * resize / 100)

#resize image
output = cv2.resize(image, (width, height))

# print(image)
# cv2.imshow("image",image)          #.imshow function shows the image
cv2.imwrite(destination, output)
# cv2.waitKey(0)                     #.waitKey(0) function keep showing image until a key is pressed






