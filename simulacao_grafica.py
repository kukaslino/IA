import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from leilao_entregas_v3 import leilao_entregas_v3

# Função para atualizar o gráfico com base nos parâmetros modificados
def atualizar(val):
    # Obtemos os parâmetros dos sliders
    prob_cruzamento = s_prob_cruzamento.val
    prob_mutacao = s_prob_mutacao.val

    # Chamamos a função de otimização
    melhor_rota, melhor_lucro = leilao_entregas_v3(conexoes, entregas, populacao_size=100, num_geracoes=100, prob_cruzamento=prob_cruzamento, prob_mutacao=prob_mutacao)

    # Atualizamos o gráfico
    ax.clear()
    ax.plot(melhor_rota + [melhor_rota[0]], 'o-')
    ax.set_title(f'Melhor Rota: {melhor_rota}\nLucro Máximo: {melhor_lucro}')
    ax.set_xticks(range(len(melhor_rota)))
    ax.set_xticklabels([f'Destino {i}' for i in melhor_rota])

# Exemplo de entrada (conexões e entregas)
conexoes = [[0, 5, 0, 2], [5, 0, 3, 0], [0, 3, 0, 8], [2, 0, 8, 0]]
entregas = {1: (0, 1), 2: (5, 10), 3: (10, 8)}

# Cria a figura e os eixos
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Adiciona sliders para modificar os parâmetros
ax_prob_cruzamento = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_prob_mutacao = plt.axes([0.25, 0.05, 0.65, 0.03])

s_prob_cruzamento = Slider(ax_prob_cruzamento, 'Prob. Cruzamento', 0.1, 1.0, valinit=0.8)
s_prob_mutacao = Slider(ax_prob_mutacao, 'Prob. Mutação', 0.1, 1.0, valinit=0.2)

# Chama a função de atualização quando os sliders são modificados
s_prob_cruzamento.on_changed(atualizar)
s_prob_mutacao.on_changed(atualizar)

# Botão de reset
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Resetar', color='lightgoldenrodyellow', hovercolor='0.975')

def reset(event):
    s_prob_cruzamento.reset()
    s_prob_mutacao.reset()
button.on_clicked(reset)

# Inicializa o gráfico
atualizar(None)

plt.show()
