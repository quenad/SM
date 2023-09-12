import cv2
import matplotlib.pyplot as plt

# Carregue a imagem
imagem = cv2.imread('sua_imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Calcule o histograma
histograma = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# Plote o histograma
plt.figure()
plt.title('Histograma')
plt.xlabel('Valores dos Pixels')
plt.ylabel('Frequência')
plt.plot(histograma)
plt.xlim([0, 256])
plt.show()
