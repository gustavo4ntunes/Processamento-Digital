import cv2
import matplotlib.pyplot as plt

# Carregamento e exibição da imagem
caminho_imagem = 'mama.jpg'
imagem = cv2.imread(caminho_imagem)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converte BGR para RGB
plt.imshow(imagem_rgb)
plt.axis('off')
plt.title('Imagem Original')
plt.show()

# Separação dos canais de cor
canal_vermelho = imagem_rgb[:, :, 0]
canal_verde = imagem_rgb[:, :, 1]
canal_azul = imagem_rgb[:, :, 2]

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(canal_vermelho, cmap='Reds')
plt.title('Canal Vermelho')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(canal_verde, cmap='Greens')
plt.title('Canal Verde')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(canal_azul, cmap='Blues')
plt.title('Canal Azul')
plt.axis('off')

plt.show()
