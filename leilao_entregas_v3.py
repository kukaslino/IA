import numpy as np
import itertools

# Função para calcular o fitness de uma rota (lucro total)
def calcular_fitness(rota, conexoes, entregas):
    lucro_total = 0
    tempo_atual = 0

    for i in range(len(rota) - 1):
        origem, destino = rota[i], rota[i+1]
        bonus = entregas[destino][1]
        tempo_entrega = conexoes[origem][destino]  # Corrigido: origem para destino
        tempo_atual += tempo_entrega

        if tempo_atual <= entregas[destino][0]:
            lucro_total += bonus

    return lucro_total


# Função para inicializar a população
def inicializar_populacao(populacao_size, entregas):
    destinos = list(entregas.keys())
    populacao = []

    for _ in range(populacao_size):
        rota = np.random.permutation(destinos)
        populacao.append(rota)

    return populacao

# Função para selecionar os indivíduos para a próxima geração (torneio)
def selecionar(populacao, conexoes, entregas):
    tamanho_torneio = 3
    torneio_indices = np.random.choice(len(populacao), tamanho_torneio)
    torneio = [populacao[i] for i in torneio_indices]

    # Escolhe o indivíduo com o melhor fitness
    melhor_rota = max(torneio, key=lambda rota: calcular_fitness(rota, conexoes, entregas))
    return melhor_rota

# Função para realizar o cruzamento (crossover) entre dois pais
def cruzamento(pai1, pai2):
    ponto_crossover = np.random.randint(1, len(pai1))
    filho1 = np.hstack((pai1[:ponto_crossover], [gene for gene in pai2 if gene not in pai1[:ponto_crossover]]))
    filho2 = np.hstack((pai2[:ponto_crossover], [gene for gene in pai1 if gene not in pai2[:ponto_crossover]]))
    return filho1, filho2

# Função para aplicar mutação em um indivíduo
def mutacao(individuo):
    gene1, gene2 = np.random.choice(len(individuo), 2, replace=False)
    individuo[gene1], individuo[gene2] = individuo[gene2], individuo[gene1]
    return individuo

# Função principal para a Versão 3 (Algoritmo Genético)
def leilao_entregas_v3(conexoes, entregas, populacao_size=100, num_geracoes=100, prob_cruzamento=0.8, prob_mutacao=0.2):
    destinos = list(entregas.keys())
    melhor_lucro = 0
    melhor_rota = None

    # Inicializa a população
    populacao = inicializar_populacao(populacao_size, entregas)

    for geracao in range(num_geracoes):
        # Avalia o fitness de cada indivíduo na população
        fitness = [calcular_fitness(individuo, conexoes, entregas) for individuo in populacao]
        melhor_fitness = max(fitness)
        indice_melhor = np.argmax(fitness)

        # Atualiza o melhor lucro e rota
        if melhor_fitness > melhor_lucro:
            melhor_lucro = melhor_fitness
            melhor_rota = populacao[indice_melhor]

        # Seleciona indivíduos para cruzamento e gera nova população
        nova_populacao = []
        for _ in range(populacao_size // 2):
            pai1 = selecionar(populacao, conexoes, entregas)
            pai2 = selecionar(populacao, conexoes, entregas)

            # Aplica cruzamento com probabilidade prob_cruzamento
            if np.random.rand() < prob_cruzamento:
                filho1, filho2 = cruzamento(pai1, pai2)
            else:
                filho1, filho2 = pai1, pai2

            # Aplica mutação com probabilidade prob_mutacao
            if np.random.rand() < prob_mutacao:
                filho1 = mutacao(filho1)
            if np.random.rand() < prob_mutacao:
                filho2 = mutacao(filho2)

            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao

    return melhor_rota, melhor_lucro

if __name__ == "__main__":
    # Exemplo de entrada (conexões e entregas)
    conexoes = [[0, 5, 0, 2], [5, 0, 3, 0], [0, 3, 0, 8], [2, 0, 8, 0]]
    entregas = {1: (0, 1), 2: (5, 10), 3: (10, 8)}

    melhor_rota, melhor_lucro = leilao_entregas_v3(conexoes, entregas, populacao_size=100, num_geracoes=100, prob_cruzamento=0.8, prob_mutacao=0.2)

    print("Melhor rota:", melhor_rota)
    print("Lucro máximo possível:", melhor_lucro)