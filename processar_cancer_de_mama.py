import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem em tons de cinza
imagem = cv2.imread('mama.jpg', cv2.IMREAD_GRAYSCALE)

_, imagem_segmentada = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY)

contagem_suspeita = np.count_nonzero(imagem_segmentada == 255)
contagem_fundo = np.count_nonzero(imagem_segmentada == 0)

percentual_suspeita = (contagem_suspeita / (contagem_suspeita + contagem_fundo)) * 100

limiar = 25
diagnostico = 'Indícios de câncer de mama detectados.' if percentual_suspeita >= limiar else 'Nenhuma evidência significativa de câncer de mama detectada.'

print(diagnostico)
print(f'Porcentagem de áreas suspeitas: {percentual_suspeita:.2f}%')

# Mostrar imagem segmentada
plt.imshow(imagem_segmentada, cmap='gray')
plt.title('Áreas Suspeitas Realçadas')
plt.axis('off')
plt.show()
