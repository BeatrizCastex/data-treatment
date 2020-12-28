""" DISTÂNCIAS INTERSÍMBOLOS
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Esse programa tenta identificar distâncias intersímbolos em um sinal discreto.
Baseado no algorítimo 1 do CDT-23:
https://www.researchgate.net/publication/339800429_Discrete_One-
Dimensional_Signals_A_Brief_Catalogue_of_Features_CDT-23
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# Arquivos que vamos abrir:
file_list = ['split_a.csv', 'split_b.csv','split_c.csv','split_e.csv',
            'split_fg2.csv']

# Arquivos que vamos escrever:
with open('inter_dist.csv', 'w') as csvfile:
    with open('number_dist.csv', 'w') as other_csvfile:
        file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        other_file = csv.writer(other_csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for f in file_list:

            inter_dist = [] # Vetor onde serão guardados os valores das distâncias
            number_dist = [] #vetor onde será guardada a quantidade de distâncias

            # Abrir o arquivo contendo o padrão
            with open(f, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                # Depois organizamos os padrões em arrays
                for row in reader:
                    walk = np.array([int(s) for s in row])

                    j = 0
                    start = 0
                    dist = 0

                    # Parseamos todo o padrão para procurar 1s:
                    for i in range(len(walk)):
                        # Quando achamos um 1 começamos a contagem de 0s:
                        if ( (walk[i] == 1) and (start == 0) ):
                            start = i
                        # Quando achamos o próximo 1 calculamos a distância e
                        # recomeçamos a contagem
                        elif ( (walk[i] == 1) ):
                            dist = (i) - start - 1
                            inter_dist.append(dist)
                            start = i
                            j += 1

                    number_dist.append(j)

            file.writerow(inter_dist)
            other_file.writerow(number_dist)
