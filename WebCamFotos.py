import cv2
import os
escolha = int(input("Escolha qual WebCam :\n(digite '0'  padrão)\n"
      "(digite '1' outra) "
      ">> "))
tempo = int(input('Tempo de espara em (segundos) >> '))
tempo = tempo * 100

nome_foto = ''
video = cv2.VideoCapture(escolha)
classificadorFace = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')
conectado , frame = video.read()
os.system('cls')
print('Conectado a WebCam: ' + str(conectado))
tirarfoto = tempo
a = 0
titulo = "Capturando Imagens - encerrar digite 'q'"

while True:
    conectado , frame = video.read()
    #print(conectado)
    #print(frame)

    if nome_foto == '':
        nome_foto = input('Digite o codigo da foto >> ')

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetctadas = classificadorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minSize=(100, 100), minNeighbors=12)

    for (x, y, l, a) in facesDetctadas:

        parametro = cv2.rectangle(frame, (x -50, y -50), (x + l + 50, y + a + 100), (0, 255, 0), 3)
        
        if a > 0:
            tirarfoto = tirarfoto - 20
            print('*')

            if (tirarfoto / 10) % 100:
                print("#")
                os.system('cls')
        else:
            print('Posicione melhor sua face na WebCam até ver um retangulo sobre ela...')

        if tirarfoto == 0 and a > 0:
            file = "fotos\image_" + nome_foto + "_.png"
            if cv2.imwrite(file, frame[(y - 50):y + (a + 100), (x - 50):x + (l + 50)]):
                os.system('cls')
                print('Arquivo %s salvo com sucesso !!!' % file)
                print()
                nome_foto = ''
                tirarfoto = tempo

            else:
                tirarfoto = tempo
                print('Erro ao tirar a foto iniciando nova contagem')


    cv2.imshow(titulo, frame)

    if cv2.waitKey(100) == ord('q'):
        break



video.release()
cv2.destroyAllWindows()