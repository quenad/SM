def rgb_to_yuv(rgb):
    # Extrai os componentes de cor R, G e B
    r, g, b = rgb

    # Calcula o componente Y (luminância)
    y = 0.299 * r + 0.587 * g + 0.114 * b

    # Calcula os componentes U e V (crominância)
    u = -0.14713 * r - 0.28886 * g + 0.436 * b
    v = 0.615 * r - 0.51498 * g - 0.10001 * b

    return (y, u, v)

# Define uma cor em RGB (por exemplo, vermelho puro)
cor_rgb = (255, 0, 0)

# Converte a cor RGB para YUV
cor_yuv = rgb_to_yuv(cor_rgb)

# Imprime os valores resultantes
print(f'Y (Luminância): {cor_yuv[0]}')
print(f'U (Crominância U): {cor_yuv[1]}')
print(f'V (Crominância V): {cor_yuv[2]}')
