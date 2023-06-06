import cv2
import numpy as np

img = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 300, 300, -1)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)
cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)