import cv2

# print("package Imported")
#
# img = cv2.imread("Resources/gradHS.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

cap = cv2.VideoCapture("Resources/golfShenanigans.mov")

while True:
    success, img = cap.read()
