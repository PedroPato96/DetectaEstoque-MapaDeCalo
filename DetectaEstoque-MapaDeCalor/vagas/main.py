import cv2
import numpy as np
import matplotlib.pyplot as plt

# Definição das regiões de interesse (ROI)
PRATELEIRAS = [[130, 304, 203, 100], [128, 455, 182, 92], [126, 565, 177, 101], [133, 681, 169, 89]]

# Constantes
LIMITE_PRATELEIRA_LIVRE = 3000
LIMITE_PRATELEIRA_OCUPADA = 3000
NUM_PRATELEIRAS = len(PRATELEIRAS)
DELAY = 50

# Matriz para armazenar contagens de ocupação
heatmap_data = np.zeros((NUM_PRATELEIRAS,), dtype=np.int32)

def processa_frame(img):
    """
    Processa a imagem para destacar as áreas de interesse.
    """
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_threshold = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img_blur = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.int8)
    img_dil = cv2.dilate(img_blur, kernel)
    return img_dil

def verifica_prateleiras(img_dil, prateleiras, heatmap_data):
    """
    Verifica o status das prateleiras e atualiza o mapa de calor.
    """
    for i, (x, y, w, h) in enumerate(prateleiras):
        recorte = img_dil[y:y+h, x:x+w]
        qt_px_branco = cv2.countNonZero(recorte)

        # Atualiza o mapa de calor com base na ocupação
        if qt_px_branco > LIMITE_PRATELEIRA_OCUPADA:
            heatmap_data[i] += 1

def gerar_mapa_de_calor(heatmap_data, prateleiras):
    """
    Gera e exibe um mapa de calor com base nos dados de ocupação.
    """
    altura = max(y + h for x, y, w, h in prateleiras)
    largura = max(x + w for x, y, w, h in prateleiras)
    heatmap = np.zeros((altura, largura), dtype=np.float32)

    for i, (x, y, w, h) in enumerate(prateleiras):
        ocupacao_normalizada = heatmap_data[i] / (max(heatmap_data) if max(heatmap_data) > 0 else 1)
        heatmap[max(0, y):min(heatmap.shape[0], y + h), max(0, x):min(heatmap.shape[1], x + w)] = ocupacao_normalizada

    plt.figure(figsize=(12, 8))
    plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    plt.colorbar(label="Ocupação Normalizada")
    plt.title("Mapa de Calor das Prateleiras")
    plt.show()

def main():
    video_path = 'DetectaEstoque-MapaDeCalor/vagas/TesteVerduras.mp4'  # Caminho correto para o vídeo
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    # Avança o vídeo para o segundo 2
    video.set(cv2.CAP_PROP_POS_MSEC, 2000)

    global heatmap_data

    while True:
        check, img = video.read()
        if not check:
            break

        img_dil = processa_frame(img)
        verifica_prateleiras(img_dil, PRATELEIRAS, heatmap_data)

        # Exibir o vídeo processado (opcional)
        for x, y, w, h in PRATELEIRAS:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Video', img)

        if cv2.waitKey(DELAY) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    # Gera o mapa de calor ao final
    gerar_mapa_de_calor(heatmap_data, PRATELEIRAS)

if __name__ == "__main__":
    main()
