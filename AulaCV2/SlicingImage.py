import numpy as np
import imutils
import cv2
img = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')
cv2.imshow("Original", img)
img_redimensionada = img[::2,::2]
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)