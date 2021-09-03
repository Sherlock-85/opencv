import cv2
import glob
# Loading and resizing images using cv2
img = cv2.imread("pleiades.jpg", 1)
print(type(img))
print(img)
print(img.shape)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Pleiades", resized_image)
cv2.imwrite("Pleiades_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# glob finds path names given a certain pattern.
# how to resize a list of images
# creates a list of images
images = glob.glob("*.jpg")
for image in images:
    img = cv2.imread(image, 1)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hello", re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized" + image, re)