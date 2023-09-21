import time
import matplotlib.pyplot as plt
from leilao_entregas_v1 import leilao_entregas_v1
from leilao_entregas_v2 import leilao_entregas_v2
from leilao_entregas_v3 import leilao_entregas_v3

def medir_tempo_execucao(funcao, *args):
    inicio = time.time()
    funcao(*args)
    fim = time.time()
    return fim - inicio

def comparacao_desempenho():
    # Exemplo de entrada (conexões e entregas)
    conexoes = [[0, 5, 0, 2], [5, 0, 3, 0], [0, 3, 0, 8], [2, 0, 8, 0]]
    entregas = {1: (0, 1), 2: (5, 10), 3: (10, 8)}

    # Número de execuções para a medição de desempenho
    NUM_EXECUCOES = 10

    # Lista para armazenar os tempos de execução
    tempos_v1 = []
    tempos_v2 = []
    tempos_v3 = []

    # Realiza as execuções e armazena os tempos
    for _ in range(NUM_EXECUCOES):
        tempo_v1 = medir_tempo_execucao(leilao_entregas_v1, conexoes, entregas)
        tempos_v1.append(tempo_v1)

        tempo_v2 = medir_tempo_execucao(leilao_entregas_v2, conexoes, entregas)
        tempos_v2.append(tempo_v2)

        tempo_v3 = medir_tempo_execucao(leilao_entregas_v3, conexoes, entregas)
        tempos_v3.append(tempo_v3)

    # Gráfico de comparação de desempenho
    plt.plot(range(1, NUM_EXECUCOES + 1), tempos_v1, label='Versão 1')
    plt.plot(range(1, NUM_EXECUCOES + 1), tempos_v2, label='Versão 2')
    plt.plot(range(1, NUM_EXECUCOES + 1), tempos_v3, label='Versão 3')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (s)')
    plt.legend()
    plt.title('Comparação de Desempenho')
    plt.show()

if __name__ == "__main__":
    comparacao_desempenho()
