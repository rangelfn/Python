import cv2
imagem = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')
recorte = imagem[0:800, 0:800]
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey(0) #espera pressionar qualquer tecla
cv2.imwrite("recorte.jpg", recorte) #salva no disco

