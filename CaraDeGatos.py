import cv2

cascade = 'cascades\\banana-classifier.xml'# delarando o cascade
classificadorGato = cv2.CascadeClassifier(cascade)# usando o algoritimo para detectar faces de gatos

arquivo = 'outros\\banana_2.jpg'# declarando a imagem
imagem = cv2.imread(arquivo)
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

detectado = classificadorGato.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=10)
print(detectado)
for (x, y, l, a) in detectado:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

cv2.imshow('Cara de Gato', imagem)
cv2.waitKey()
