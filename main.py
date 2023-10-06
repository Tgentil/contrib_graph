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

# Calculando as posições iniciais e finais para a letra H
X_LINHA = LARGURA // 2 - 1  # início da primeira linha vertical da letra H
X_LINHA_FIM = LARGURA // 2 + 1  # fim da segunda linha vertical da letra H

Y_LINHA = ALTURA // 2 - 1  # início da linha horizontal da letra H
Y_LINHA_FIM = ALTURA // 2 + 1  # fim da linha horizontal da letra H

# Ajustando a altura da letra H para ter um pixel de margem na parte superior e inferior
Y_INICIO = 1  # início da primeira linha vertical da letra H
Y_FIM = ALTURA - 2  # fim da segunda linha vertical da letra H

# Reinicializando a matriz
matriz = np.ones((ALTURA, LARGURA))

# Preenchendo a matriz para formar a letra H
# Linhas verticais da letra H
for i in range(Y_INICIO, Y_FIM + 1):
    matriz[i][X_LINHA] = 0
    matriz[i][X_LINHA_FIM] = 0

# Linha horizontal da letra H
for j in range(X_LINHA, X_LINHA_FIM + 1):
    matriz[ALTURA // 2][j] = 0

# Chamando a função para visualizar o desenho
plot_github_style(matriz)
