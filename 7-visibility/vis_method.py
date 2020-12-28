''' MÉTODO DE VISIBILIDADE
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Este programa tem como objetivo transformar um sinal em uma rede através do
método de visibilidade usando o algorítimo 3 do CDT-23 e então calcular o grau
e coeficiente de aglomeração dos grafos, suas médias e desvios padrões.

Referências:
https://www.researchgate.net/publication/339800429_Discrete_One-
Dimensional_Signals_A_Brief_Catalogue_of_Features_CDT-23
https://ocw.mit.edu/courses/engineering-systems-division/esd-342-network-
representations-of-complex-engineering-systems-spring-2010/readings/MITESD_
342S10_ntwk_models.pdf
https://www.geeksforgeeks.org/clustering-coefficient-graph-theory/
https://networkx.github.io/documentation/stable/
'''

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv

# Primeiro abrimos nosso sinal:
with open('aut_fg2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # Depois organizamos o sinal em arrays
    for row in reader:
        signal = np.array([int(s) for s in row])

# Então criamos um grafo vazio:
G = nx.Graph()
G.add_node( i for i in range(len(signal)))

# Em seguida implementamos o algorítimo do método de visibilidade
for j in range(2, len(signal)):
    for i in range(1, (j-1)):
        flag = 1
        k = i + 1
        while ( (k <= (j -1)) and (flag == 1) ):
            aux = signal[j] + (signal[i] - signal[j]) * (j-k)/(j-i)
            if (signal[k] >= aux):
                flag = 0
            k += 1
        if ( flag == 1 ):
            G.add_edges_from([ (i,j), (j,i) ])

# Vamos calcular a média e desvio padrão dos graus  e do coeficiente de
# aglomeração do grafo
deg = []
agl = []
# Para cada nódulo
for i in G.nodes():
    # Obter grau:
    deg.append(G.degree(i))
    # Obter coeficiente de alomeração
    agl.append(nx.clustering(G,i))

# Calculando a média e o desvio padrão dos dados
mean_deg = np.mean(deg)
std_deg = np.std(deg)
mean_agl = np.mean(agl)
std_agl = np.std(agl)


print('\n Método de visibilidade para o autômato do CDT-23')
print('\n Grau dos nódulos: \n Média: ', mean_deg)
print(' Desvio padrão:', std_deg)
print('\n Coeficiente de aglomeração dos nódulos: \n Média: ', mean_agl)
print(' Desvio padrão:', std_agl, '\n')


# Desenhando o grafo gerado:
nx.draw_random(G, node_color='black', node_size=50, width=0.5)
plt.show()
