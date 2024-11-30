import cv2

# Lista para armazenar as coordenadas das vagas
vagas = []

# Função de callback para capturar as regiões clicadas
def selecionar_vaga(event, x, y, flags, param):
    global vagas, ponto_inicial, desenhando

    if event == cv2.EVENT_LBUTTONDOWN:
        ponto_inicial = (x, y)
        desenhando = True

    elif event == cv2.EVENT_MOUSEMOVE and desenhando:
        imagem_temp = img.copy()
        cv2.rectangle(imagem_temp, ponto_inicial, (x, y), (0, 255, 0), 2)
        cv2.imshow("Selecionar Vagas", imagem_temp)

    elif event == cv2.EVENT_LBUTTONUP:
        desenhando = False
        ponto_final = (x, y)
        x1, y1 = ponto_inicial
        x2, y2 = ponto_final
        x, y = min(x1, x2), min(y1, y2)
        w, h = abs(x1 - x2), abs(y1 - y2)
        vagas.append([x, y, w, h])
        print(f"Vaga adicionada: {x, y, w, h}")
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Carregar o vídeo
video_path = 'vagas/TesteVerduras.mp4'
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Erro ao abrir o vídeo: {video_path}")
else:
    # Ler um quadro em um ponto específico do vídeo (por exemplo, no segundo 2)
    video.set(cv2.CAP_PROP_POS_MSEC, 2000)
    _, img = video.read()
    video.release()

    desenhando = False
    ponto_inicial = None

    cv2.imshow("Selecionar Vagas", img)
    cv2.setMouseCallback("Selecionar Vagas", selecionar_vaga)
    print("Clique e arraste para desenhar as regiões de interesse (vagas). Pressione 'q' para sair.")

    while True:
        cv2.imshow("Selecionar Vagas", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    print("Coordenadas finais das vagas:")
    print(vagas)
