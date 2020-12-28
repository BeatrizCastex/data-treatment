""" SPLIT SIGNALS
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Esse programa tenta obter gráficos de split signal dado um padrão gerado
por certo autômato.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt


# Arquivos que vamos abrir:
file_list = ['aut_a_1000.csv', 'aut_b_1000.csv','aut_c_1000.csv',
             'aut_e_1000.csv', 'aut_fg2_1000.csv']

# Arquivos que vamos escrever:
write_list = ['split_a.csv', 'split_b.csv','split_c.csv','split_e.csv',
             'split_fg2.csv']

j = 0

for f in file_list:
    # Abrir arquivo onde vamos escrever:
    with open(write_list[j], 'w') as csvfile:
        file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        j += 1
        # Abrir o arquivo contendo o padrão
        with open(f, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            # Depois organizamos os padrões em arrays
            for row in reader:
                walk = np.array([int(s) for s in row])

                # Arrays onde serão armazenados os padrões de frequência dos sinais
                ss_0 = []
                ss_1 = []

                # Então buscamos o array para cada um dos sinais do padrão:
                for i in range(len(walk)):
                    if ( walk[i] == 0):
                        ss_0.append(1)
                        ss_1.append(0)
                    elif (walk[i] == 1):
                        ss_0.append(0)
                        ss_1.append(1)
                    else:
                        ss_0.append(0)
                        ss_1.append(0)

                file.writerow(ss_1)
