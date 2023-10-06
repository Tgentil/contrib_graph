""" Cria um gráfico no estilo do quadro de contribuições do GitHub.
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_github_style(matrix):
    """
    Plota uma matriz no estilo do quadro de contribuições do GitHub.
    
    A função visualiza uma matriz onde valores 1 representam dias com commits (verde) e 
    valores 0 representam dias sem commits (branco). A visualização é feita usando o 
    matplotlib e imita o estilo do quadro de contribuições do GitHub.

    Args:
        matrix (numpy.ndarray): Matriz 2D (7xN) de contribuições, onde cada elemento 
        é 1 (dia com commit) ou 0 (dia sem commit).
    """
    ax = plt.subplots(figsize=(13, 7))[1]

    # Desenhando cada quadrado
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            color = "#eeeeee" if matrix[y, x] == 1 else "green"
            rect = plt.Rectangle((x*1.2, y*1.2), 1, 1, facecolor=color, edgecolor="gray")
            ax.add_patch(rect)

    # Configurando o gráfico
    ax.set_xlim(0, matrix.shape[1]*1.2)
    ax.set_ylim(0, matrix.shape[0]*1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.gca().invert_yaxis()
    plt.title("Quadro de Contribuições do GitHub")
    plt.show()

if __name__ == '__main__':
    # Definindo o tamanho da matriz
    ALTURA = 7
    LARGURA = 52

    # Criando uma matriz 7x52 preenchida com 1s (representando commits)
    matriz = np.ones((ALTURA, LARGURA))

    # Chamando a função para visualizar o quadro
    plot_github_style(matriz)
