import numpy as np
import matplotlib.pyplot as plt

# --- Parâmetros da Simulação ---
LARGURA = 401  # Número de células na grade 1D (use um número ímpar para centralizar)
GERACOES = 128 # Número de passos de tempo (altura da imagem)

def aplicar_regra90(vizinhanca):
    """
    Aplica a Regra 90 do autômato celular elementar.
    O novo estado é o XOR (ou soma módulo 2) dos vizinhos esquerdo e direito.
    
    Tabela da Regra 90:
    Padrão:   111 110 101 100 011 010 001 000
    Resultado: 0   1   0   1   1   0   1   0
    
    Args:
        vizinhanca (tuple): Uma tupla de 3 elementos (vizinho_esq, centro, vizinho_dir)
                            com os estados (0 ou 1).
    
    Returns:
        int: O novo estado da célula central (0 ou 1).
    """
    vizinho_esq, _, vizinho_dir = vizinhanca
    return (vizinho_esq + vizinho_dir) % 2

def simular_automato_celular(largura, geracoes):
    """
    Executa a simulação do autômato celular 1D.
    
    Args:
        largura (int): A largura da grade.
        geracoes (int): O número de gerações a simular.
        
    Returns:
        numpy.ndarray: Uma matriz 2D representando a evolução tempo-espaço do autômato.
    """
    # Inicializa a grade com todas as células em 0 (inativas)
    grid = np.zeros((geracoes, largura), dtype=np.int8)
    
    # Condição Inicial: uma única célula ativa no centro da primeira geração
    grid[0, largura // 2] = 1
    
    # Itera através das gerações para construir o padrão
    for t in range(geracoes - 1):
        for i in range(largura):
            # Obtém os estados da vizinhança da geração anterior (t)
            # Trata as condições de contorno (células fora da grade são sempre 0)
            vizinho_esq = grid[t, i - 1] if i > 0 else 0
            centro = grid[t, i]
            vizinho_dir = grid[t, i + 1] if i < largura - 1 else 0
            
            vizinhanca = (vizinho_esq, centro, vizinho_dir)
            
            # Calcula e define o novo estado da célula na próxima geração (t+1)
            grid[t + 1, i] = aplicar_regra90(vizinhanca)
            
    return grid

def visualizar_grid(grid):
    """
    Visualiza a grade do autômato celular usando Matplotlib.
    
    Args:
        grid (numpy.ndarray): A matriz 2D da simulação.
    """
    plt.figure(figsize=(12, 12 * (GERACOES / LARGURA)))
    # Usamos 'binary' (ou 'gray_r') para que 1=preto e 0=branco
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.title(f'Triângulo de Sierpiński gerado pela Regra 90 ({GERACOES} gerações)')
    plt.xlabel('Células')
    plt.ylabel('Gerações (Tempo)')
    plt.xticks([]) # Remove marcações do eixo x
    plt.yticks([]) # Remove marcações do eixo y
    plt.show()

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    print("Iniciando a simulação do autômato celular para gerar o Triângulo de Sierpiński...")
    grid_resultado = simular_automato_celular(LARGURA, GERACOES)
    print("Simulação concluída. Exibindo o resultado...")
    visualizar_grid(grid_resultado)