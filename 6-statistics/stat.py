''' DADOS ESTATÍSTICOS DOS AUTÔMATOS
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Este programa tem como objetivo calcular dados como a média, desvio padrão,
evenness, entropia, etc. de features que retiramos de padrões formados por
nossos autômatos, como número de bursts num split signal, por exemplo.

Se houver algum conjunto de valores que não seja necessário ou possível
calcular, apenas desativálos com comentários.

'''
import numpy as np
import matplotlib.pyplot as plt
from math import log
import csv

i = 0

# Função gaussiana


def gaussian(x, mu, sig):
    return 1 / (np.sqrt(2 * np.pi) * sig) * np.exp(-(((x - mu) / sig)**2) / 2)


# Bins que serão usados para plotar a gaussiana:
bins = np.linspace(-0.05, 0.05, 1000)

# Vetores onde iremos guardar os dados para fazer gráficos:
gaus = []  # Dados das gaussianas

# Primeiro abrimos o arquivo e lemos os dados coletados para cada automato:

file_name = 'inter_dist.csv'  # !!! INSIRA AQUI NOME DO ARQUIVO !!!
print('\nDistâncias intersinais')  # Dados sendo análisados

# Os arquivos estão organizados de forma que cada linha tem os dados de
# um dos nossos autômatos.
with open(file_name, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # Depois organizamos os padrões em arrays
    for row in reader:
        # Salvamos os dados
        dados = np.array([float(s) for s in row])

        # Identificamos o autômato em que estamos trabalhando
        if (i == 0):
            aut = 'a:'
        elif (i == 1):
            aut = 'b:'
        elif (i == 2):
            aut = 'c:'
        elif (i == 3):
            aut = 'e:'
        else:
            aut = 'do CDT-23:'

        print('\nDados do autômato ' + aut)

        ''' MÉDIA, DESVIO E GAUSSIANA '''

        # Calculando a média e o desvio padrão dos dados
        mean = np.mean(dados)
        sdev = np.std(dados)

        # Mapeando a densidade de probabilidade normal (gaussiana):
        gaus.append(gaussian(bins, mean, sdev))

        # Imprimindo valores:
        print('Média: ', mean)
        print('Desvio Padrão: ', sdev)

        ''' ENTROPIA E EVENNESS '''

        # Calculando a entropia dos dados:
        entp = 0
        for x in range(len(dados)):
            if (dados[x] != 0):
                entp -= dados[x] * log(dados[x], 2)

        # Calculando a envenness dos dados:
        evns = 2**entp

        # Imprimindo valores:
        print('Entropia: ', entp)
        print('Evenness: ', evns)

        i = i + 1


# Montando o gráfico da gaussiana:
j = 0
for y in gaus:
    # Identificando o autômato:
    if (j == 0):
        colors, labels = 'orange', 'Autômato A'
    elif (j == 1):
        colors, labels = 'limegreen', 'Autômato B'
    elif (j == 2):
        colors, labels = 'blue', 'Autômato C'
    elif (j == 3):
        colors, labels = 'yellow', 'Autômato E'
    else:
        colors, labels = 'red', 'Autômato CDT-23'

    plt.plot(bins, y, label=labels, color=colors)

    j = j + 1

# Plotando o gráfico
plt.xlabel('Distâncias intersinais')  # NOME DOS DADOS ANALISADOS
plt.ylabel('Densidade de probabilidade normal')
plt.legend()
plt.show()
