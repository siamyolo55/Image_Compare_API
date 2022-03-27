import cv2

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#img = cv2.imread('Jk.PNG')
img = cv2.imread('0001.jpg')

# color conversion od image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# image_to_string
# print(pytesseract.image_to_string(img))
# image_to_boxes
# print(pytesseract.image_to_boxes(img))
# #Detecting Characters
# hImg, wImg, _ = img.shape
# # cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img)  # ,config=cong)
# # split the Characters
# for a in boxes.splitlines():
#     # print(a)
#
#     a = a.split(' ')
#     print(a)
#     # get the information
#     x, y, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])  # use these values
#     # to create a rectangle and to put the text
#     cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)  # red color(0,0,255) thickness(1)
#
#     # labels the characters
#     cv2.putText(img, a[0], (x, hImg - y + 5), cv2.FONT_HERSHEY_COMPLEX, .25, (255, 0, 0),
#
# Detecting numbers/words
hImg, wImg, _ = img.shape
#cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img)#, config=cong)
print(boxes)
# create counter
for x, a in enumerate(boxes.splitlines()):
    if x != 0:
        a = a.split()
        print(a)
    # get the information
    if len(a) == 12:
        x, y, w, h = int(a[6]), int(a[7]), int(a[8]), int(a[9])  # use these values
        #      #to create a rectangle and to put the text
        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)  # red color(0,0,255) thickness(1)
        #
        # #labels the characters
        cv2.putText(img, a[11], (x, y + 35), cv2.FONT_HERSHEY_COMPLEX, .5, (255, 0, 0),
                    1)  # 1st (1) is scale. 2nd (1) is thic

result = cv2.imwrite('Result.jpg', img)
cv2.waitKey(0)