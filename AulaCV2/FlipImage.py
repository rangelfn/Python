import cv2
img = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')
cv2.imshow("Original", img)
flip_horizontal = img[::-1,:]
#comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)

cv2.imshow("Flip Horizontal", flip_horizontal)
flip_vertical = img[:,::-1]
#comando equivalente abaixo
#flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical)

flip_hv = img[::-1,::-1]
#comando equivalente abaixo
#flip_hv = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)
cv2.waitKey(0)