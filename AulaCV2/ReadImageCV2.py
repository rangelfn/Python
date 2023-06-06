# Importação das bibliotecas
import cv2
import numpy

# Leitura da imagem
imagem = cv2.imread('C:\\00Compartilhada\\3P-ADS_Noturno\\Python\\img_predios_colorida.jpg')

#Largura da Imagem
print('Largura em pixels: ', end='')
print(imagem.shape[1])

#Altura da Imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])

#Quantidade de Canais
print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("Imagem Carregada", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
