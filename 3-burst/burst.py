""" SPLIT SIGNALS
Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
05/2020

Esse programa tenta identificar bursts em um sinal discreto. Baseado no
algorítimo 1 do CDT-23:
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
with open('length_burst.csv', 'w') as csvfile:
    with open('number_burst.csv', 'w') as other_csvfile:
        file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        other_file = csv.writer(other_csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for f in file_list:

            length_burst = [] # Vetor onde serão guardados os comprimentos
            number_burst = [] #vetor onde será guardada a quantidade de bursts

            # Abrir o arquivo contendo o padrão
            with open(f, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                # Depois organizamos os padrões em arrays
                for row in reader:
                    walk = np.array([int(s) for s in row])

                    burst = [] # Vetor onde serão guardados os índices
                    j = 0

                    # Parseamos todo o padrão para procurar 1s:
                    for i in range(len(walk)):
                        # Quando achamos um 1 contamos:
                        if ( walk[i] == 1 ):
                            j += 1
                        # Para não dar erro de índice pulamos o primeiro e o último:
                        elif ( i == 0 ):
                            pass
                        elif ( i == 1000 ):
                            # Mas antes vemos se o último é o fim de um burst
                            if ( walk[i-1] == 1 ):
                                burst.append(i-1)
                                length_burst.append(j)
                                j = 0
                            else:
                                pass
                        # Se estiver entre dois 1s o zero faz parte do burst
                        elif ( (walk[i-1] == 1 ) and (walk[i+1] == 1) ):
                            j += 1
                        # Se não reiniciamos o contador e marcamos  os valores
                        elif ( walk[i-1] == 1 ):
                            length_burst.append(j)
                            burst.append(i-1)
                            j = 0

                    number_burst.append(len(burst))

            file.writerow(length_burst)
            other_file.writerow(number_burst)
