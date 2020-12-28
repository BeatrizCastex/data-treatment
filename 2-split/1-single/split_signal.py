""" SPLIT SIGNALS
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Esse programa tenta obter gráficos de split signal dado um padrão gerado
por certo autômato.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# Arrays onde serão armazenados os padrões de frequência dos sinais
ss_0 = []
ss_1 = []

# Abrir o arquivo contendo o padrão
with open('aut_a.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # Depois organizamos os padrões em arrays
    for row in reader:
        walk = np.array([int(s) for s in row])

# Então buscamos o array para cada um dos sinais do padrão:
for i in range(len(walk)):
    if ( walk[i] == 0):
        ss_0.append(1)
        ss_1.append(0)
    else:
        ss_0.append(0)
        ss_1.append(1)


# Finalmente plotamos os gráficos de barra contínua:
x = list(range(0, len(walk))) # Cria uma lista com todos os índices de walk
# Criamos uma figura formada de dois gráficos em uma coluna:
fig, ax= plt.subplots(nrows=2, ncols=1,figsize=(9,3), constrained_layout=True)
fig.suptitle('Split Signal - Autômato A', fontsize=14)

ax[0].bar(x,ss_0, color="#d87a00")
ax[0].set_title('0')
ax[0].set_ylim(0,1) # Limitamos o tamanho do eixo y
ax[0].set_xlim(0,190) # Limitamos o tamanho do eixo x
ax[0].set_facecolor('#191970') # mudamos o plano de fundo

ax[1].bar(x,ss_1, color="#d87a00")
ax[1].set_title('1')
ax[1].set_ylim(0,1) # Limitamos o tamanho do eixo y
ax[1].set_xlim(0,190) # Limitamos o tamanho do eixo x
ax[1].set_facecolor('#191970') # mudamos o plano de fundo

plt.show()
