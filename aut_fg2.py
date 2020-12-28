""" TESTE AUTÔMATO 2
  Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
  05/2020

  Nesse programa representamos autômatos probabilisticos como matrizes
  e os utilizamos para gerar padões que serão salvos em arquivos para análise.
  O objetivo é ser capaz de gerar padrões com qualquer** autômato
  probabilistico usando esse programa.

  Consulta para método de escolha de estado:
  https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial
  Consulta para escrita de arquivo:
  https://docs.python.org/2/library/csv.html

  ** muito cuidado ao dizer qualquer, pode ser que tenha algum não testado
  que não funcione.
  """

import numpy as np
import csv

# abrir o arquivo para onde vamos importar os padrões
with open('aut_fg2_1000.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Quais são os possíveis estados?
    possible_states = np.array([0, 1, 2, 3])

    # Criar a matriz de transição de probabilidade que representa o autômato:
    # No caso essa matriz mostra as chances de mudar de estado como a seguir:
    # [ (0 ficar no 0)  (1 ir pra o 0)]
    # [ (0 ir pra o 1)  (1 ficar no 1)]
    auto = np.array([[0.5, 0.0, 0.0, 0.7],
                     [0.5, 0.1, 0.0, 0.0],
                     [0.0, 0.9, 0.6, 0.0],
                     [0.0, 0.0, 0.4, 0.3]])

    N = 200 # Quantos padrões você quer gerar?
    L = 1000 # Quantos passos você quer que o padrão tenha?

    start = 0 # Nódulo inicial

    for step in range(N):

        # Definir condições iniciais

        walk = [start] # Vetor onde será guardado o caminho
        state = [1,0,0,0] # Estado inicial

        for step in range(L):

            # Definir a probabilidade de ir para cada estado:
            prob = auto.dot(state) # multiplicamos o autômato com o estado atual

            # Escolher um caminho:
            # Para isso usamos a função de escolha aleatória do numpy para escolher um
            # dos possíveis estados com as probabilidades definidas.
            i = np.random.choice(possible_states, replace=True, p=prob)
            # marcamos o nódulo em que estamos no caminho:
            walk.append(i)

            # Definir novo estado:
            if (i == 0):
                state = [1, 0, 0, 0]
            elif (i == 1):
                state = [0, 1, 0, 0]
            elif (i == 2):
                state = [0, 0, 1, 0]
            else:
                state = [0, 0, 0, 1]

        # Agora salvamos o caminho num arquivo:
        file.writerow(walk)
