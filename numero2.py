import openCV
import numpy as np

# Defina uma cor em RGB (por exemplo, vermelho puro)
cor_rgb = np.uint8([[[255, 0, 0]]])

# Converta a cor RGB para HSV
cor_hsv = cv2.cvtColor(cor_rgb, cv2.COLOR_RGB2HSV)

# Extraia os valores de Hue, Saturation e Value
h, s, v = cor_hsv[0][0]

# Imprima os valores resultantes
print(f'Hue (Matiz): {h}')
print(f'Saturation (Saturação): {s}')
print(f'Value (Valor): {v}')
