import cv2
import time
from emailing import send_email
import glob, os
from threading import Thread

# array = cv2.imread("image.png")
# print(array.shape)
# print(array)

video = cv2.VideoCapture(0)
time.sleep(1)


firstFrame = None
statusList = []
count = 1


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


while True:
    status = 0
    check, frame = video.read()
    # cv2.imshow("My video", frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray_frame_gau

    deltaFrame = cv2.absdiff(firstFrame, gray_frame_gau)
    threshFrame = cv2.threshold(deltaFrame, 60, 255, cv2.THRESH_BINARY)[1]
    dilateFrame = cv2.dilate(threshFrame, None, iterations=2)
    cv2.imshow("My video", dilateFrame)

    contours, check = cv2.findContours(dilateFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1

            allImages = glob.glob("images/*.png")
            index = int(len(allImages)/2)
            image_object = allImages[index]

            statusList.append(status)
            statusList = statusList[-2:]

    if statusList[0] == 1 and statusList[1] == 0:
        email_thread = Thread(target=send_email, args=(image_object,))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
clean_thread.start()




