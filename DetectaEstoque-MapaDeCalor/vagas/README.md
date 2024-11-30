### README.md

# Monitoramento de Ocupação por Visão Computacional

Este projeto utiliza técnicas de visão computacional para monitorar a ocupação de áreas específicas, como displays de produtos, processando quadros de um vídeo e gerando um mapa de calor dinâmico para indicar o status das regiões de interesse (ROIs).

## Funcionalidades

1. **Processamento de Vídeo**:
   - Processa os quadros do vídeo para detectar mudanças nas ROIs.
   - Exibe as regiões destacadas no vídeo.

2. **Mapa de Calor Dinâmico**:
   - Gera um mapa de calor que reflete a ocupação ao longo do vídeo.

3. **Detecção de Alterações**:
   - Sensível a mudanças de objetos pequenos, como retirada e reposição de itens.

## Requisitos

- Python 3.7 ou superior.
- Bibliotecas:
  - `opencv-python`
  - `numpy`
  - `matplotlib`

Para instalar as dependências:
```bash
pip install opencv-python numpy matplotlib
```

## Estrutura do Código

### Processamento de Quadros
A função `processa_frame` aplica operações de processamento de imagem para destacar as áreas de interesse. As etapas incluem:

1. **Conversão para Escala de Cinza**.
2. **Limiarização Adaptativa**: Para destacar objetos brancos sobre fundo preto.
3. **Desfocagem Mediana**: Reduz o ruído preservando bordas.
4. **Detecção de Bordas**: Utiliza o filtro Canny para realçar as alterações.
5. **Dilatação**: Une regiões próximas, tornando os objetos mais contínuos.

### Verificação de Ocupação
A função `verifica_vagas` avalia o status de cada ROI, determinando se está ocupada com base no número de pixels brancos.

### Geração do Mapa de Calor
A função `gerar_mapa_de_calor` cria um mapa de calor dinâmico que reflete a ocupação das ROIs em tempo real.

## Como Usar

1. **Defina o Vídeo e as ROIs**:
   Atualize o caminho do vídeo na variável `video_path` e configure as coordenadas das ROIs na variável `VAGAS`. Por exemplo:
   ```python
   VAGAS = [[130, 304, 203, 100], [128, 455, 182, 92], [126, 565, 177, 101], [133, 681, 169, 89]]
   ```

2. **Execute o Script**:
   ```bash
   python monitoramento.py
   ```

3. **Interaja com a Janela do Vídeo**:
   - O vídeo será exibido com as ROIs destacadas.
   - Pressione `q` para sair.

4. **Analise o Mapa de Calor**:
   - Após o processamento, o mapa de calor será exibido em uma nova janela.

## Exemplo de Saída

- **Vídeo**: As ROIs são destacadas com cores que indicam o status (livre ou ocupado).
- **Mapa de Calor**:
  ![Exemplo de Mapa de Calor](https://via.placeholder.com/600x400.png?text=Mapa+de+Calor)

## Personalização

### Ajuste de Limites
Os limites para determinar se uma ROI está ocupada podem ser ajustados conforme o cenário:
```python
LIMITE_VAGA_LIVRE = 50
LIMITE_VAGA_OCUPADA = 500
```

### Seleção de Novas ROIs
Use o script `Seleciona Vagas.py` para configurar novas regiões de interesse com base em um quadro específico do vídeo:
```bash
python Seleciona Vagas.py
```

### Integração
Este projeto pode ser adaptado para diferentes cenários, como monitoramento de produtos em prateleiras, ocupação em eventos ou análise de tráfego.

## Licença
Este projeto é disponibilizado sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário. 

---

Para dúvidas ou sugestões, entre em contato!