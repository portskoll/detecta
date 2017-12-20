def detect(image):
 image_faces = []
 bitmap = cv2.fromarray(image)
 faces = cv2.HaarDetectObjects(bitmap, cascade, cv.CreateMemStorage(0))
 if faces:
  for (x,y,w,h),n in faces:
   image_faces.append(image[y:(y+h), x:(x+w)])
   #cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)
 return image_faces

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    while 1:
        _,frame =cam.read()
        image_faces = []
        image_faces = detect(frame)
        for i, face in enumerate(image_faces):
           cv2.imwrite("face-" + str(i) + ".jpg", face)

        #cv2.imshow("features", frame)
        if cv2.waitKey(1) == 0x1b: # ESC
            print 'ESC pressed. Exiting ...'
            break