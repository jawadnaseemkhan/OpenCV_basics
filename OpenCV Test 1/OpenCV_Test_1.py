#from curses.textpad import rectangle
import cv2

testImage = cv2.imread("test.jpeg")

x, y = testImage.shape[:2]                              #For getting the detail about the dimesions of picture
print("Height = {}, Width = {}".format(x,y))

(R,G,B) = testImage[480, 250]                           #For getting the RGB values 
print("R = {}, G = {}, B = {}".format(R,G,B))

b = testImage[480, 250, 1 ]                             #For getting the single value
print("b = {}".format(b))

(h, w, d) = testImage.shape                             #For getting the three values of dimension along with the depth of image
print("Width = {}, Height = {}, Depth = {}".format(h,w,d) )

size = cv2.resize(testImage, (1920,1080))               #For resizing the image
cv2.imwrite("test1.jpg",testImage)

rectangle = cv2.rectangle(testImage,(400,400),(600,600),(255,255,0),8)          #for inserting the rectangle inside the image
cv2.imwrite("test1.jpg",testImage)

text_input = cv2.putText(testImage,"Hello World",(50,150),cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),4) #for writing the text inside the image
cv2.imwrite("test1.jpg",testImage)


cv2.imshow("TestImage",testImage)
