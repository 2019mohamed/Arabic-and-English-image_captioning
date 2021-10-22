# # import cv2

# # capture = cv2.VideoCapture(r'C:\Users\2tech\Documents\workspace\Python\video segment\videoplayback(1).mp4')
# # frameNr = 0
# # frameNr = 0
# # while (True):
# #     # process frames
# #     success, frame = capture.read()
# #     frame_[frameNumber]
# #     cv2.imwrite('C:/Users/2tech/Documents/workspace/Python/video segment/frame_{frameNr}.jpg', frame)

# # frameNr = frameNr+1
# # capture.release()



# # import cv2
 
# # capture = cv2.VideoCapture(r'C:\Users\2tech\Documents\workspace\Python\video segment\videoplayback(1).mp4')
 
# # frameNr = 0
 
# # while (True):
 
# #     success, frame = capture.read()
 
# #     if success:
# #         cv2.imwrite(f'C:/Users/2tech/Documents/workspace/Python/video segment/frame_{frameNr}.jpg', frame)
 
# #     else:
# #         break
 
# #     frameNr = frameNr+1
 
# # capture.release()


# import cv2
 
# # Opens the Video file
# cap= cv2.VideoCapture(r'C:\Users\2tech\Documents\workspace\Python\video segment\videoplayback(1).mp4')
# i=0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == False:
#         break
#     cv2.imwrite('kang'+str(i)+'.jpg',frame)
#     i+=1
 
# cap.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np
import os



# Playing video from file:
cap = cv2.VideoCapture('testing2.mp4')


try:
    if not os.path.exists('secondtest'):
        os.makedirs('secondtest')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
     
    ret, frame = cap.read()
    

    # Saves image of the current frame in jpg file
    name = './secondtest/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
   

    # To stop duplicate images
    currentFrame += 1
    

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()