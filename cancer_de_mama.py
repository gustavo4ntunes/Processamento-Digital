from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np
import matplotlib.pyplot as plt

# Abrir a imagem de mamografia
imagem = Image.open('original_mama.jpg')
imagem_cinza = imagem.convert('L')

array_imagem = np.array(imagem_cinza)
contornos = measure.find_contours(array_imagem, level=0.8)

# Desenhar os contornos na imagem original
desenho_imagem = ImageDraw.Draw(imagem)
for contorno in contornos:
    pares_pontos = list(zip(contorno[:-1], contorno[1:]))
    for ponto_atual, proximo_ponto in pares_pontos:
        desenho_imagem.line(
            [ponto_atual[1], ponto_atual[0], proximo_ponto[1], proximo_ponto[0]],
            fill='blue',
            width=2,
        )

contraste_ajustado = ImageEnhance.Contrast(imagem)
imagem_contraste = contraste_ajustado.enhance(16.0)

imagem_contraste.save('imagem_mama_contornada.jpg')

# Exibir a imagem final com os contornos e contraste elevado
plt.imshow(imagem_contraste, cmap='gray')
plt.title('Mamografia com Contornos e Contraste Ajustado')
plt.axis('off')
plt.show()
