import cv2


classificador = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')
imagem = cv2.imread('pessoas\des.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=4, minSize=(30,30))



for x, y, l, a in facesDetectadas:

    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 1)

cv2.imshow("Faces Detectadas", imagem)
cv2.waitKey()