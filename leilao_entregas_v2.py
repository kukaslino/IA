# Importe as bibliotecas necessárias para a Versão 2
import itertools

# Função para calcular o lucro total para uma determinada ordem de entregas
def calcular_lucro(ordem_entregas, conexoes, entregas):
    lucro_total = 0
    tempo_atual = 0

    for entrega in ordem_entregas:
        destino = entrega
        bonus = entregas[destino][1]
        tempo_entrega = conexoes[tempo_atual][destino]  # Tempo até o destino
        tempo_atual += tempo_entrega  # Tempo total até a entrega
        if tempo_atual <= entregas[destino][0]:  # Entrega dentro do horário
            lucro_total += bonus
        else:
            break

    return lucro_total

# Função para obter todas as permutações possíveis das entregas
def obter_permutacoes(entregas):
    permutacoes = []
    for entrega in itertools.permutations(entregas):
        permutacoes.append(list(entrega))
    return permutacoes

# Função principal para a Versão 2
def leilao_entregas_v2(conexoes, entregas):
    melhor_lucro = 0
    melhor_ordem_entregas = []

    # Obtém todas as permutações possíveis das entregas
    permutacoes_entregas = obter_permutacoes(entregas)

    # Calcula o lucro para cada ordem de entregas e encontra a melhor
    for ordem_entregas in permutacoes_entregas:
        lucro_atual = calcular_lucro(ordem_entregas, conexoes, entregas)
        if lucro_atual > melhor_lucro:
            melhor_lucro = lucro_atual
            melhor_ordem_entregas = ordem_entregas

    return melhor_ordem_entregas, melhor_lucro

if __name__ == "__main__":
    # Exemplo de entrada (conexões e entregas)
    conexoes = [[0, 5, 0, 2], [5, 0, 3, 0], [0, 3, 0, 8], [2, 0, 8, 0]]
    entregas = {1: (0, 1), 2: (5, 10), 3: (10, 8)}

    ordem_entregas, lucro = leilao_entregas_v2(conexoes, entregas)

    print("Melhor ordem de entregas:", ordem_entregas)
    print("Lucro total:", lucro)
