import cv2

img = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')

#captura altura e largura
(alt, lar) = img.shape[:2]

#acha o centro
centro = (lar // 2, alt // 2)

M = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
cv2.waitKey(0)