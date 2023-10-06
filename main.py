""" Exemplo de uso da função plot_github_style para criar um desenho no estilo do GitHub.
"""
import numpy as np
from create_graph import plot_github_style

# Definindo o tamanho da matriz
ALTURA = 7
LARGURA = 52

# Criando uma matriz 7x52 preenchida com 1s (representando commits)
matriz = np.ones((ALTURA, LARGURA))

# Aqui, você pode modificar a matriz conforme desejar para criar seu desenho.
# Por exemplo, para criar uma linha diagonal:
for i in range(min(ALTURA, LARGURA)):
    matriz[i][i] = 0  # Pintando alguns quadrados de verde

# Chamando a função para visualizar o desenho
plot_github_style(matriz)
