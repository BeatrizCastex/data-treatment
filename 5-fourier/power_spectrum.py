""" ESPECTRO DE POTÊNCIA E FFT
  Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
  05/2020

  Esse programa tem como objetivo fazer uma transformada de fourier de um
  conjunto de split signals e através disso calcular seu espectro de potência.

  Referências:
  https://personal.egr.uri.edu/chelidz/documents/mce567_Chapter_4.pdf
  https://www.youtube.com/watch?v=uDz-KirOmw8
  https://www.youtube.com/watch?v=P571FXS33wg
  https://numpy.org/doc/1.18/reference/generated/numpy.fft.fft.html
  https://www.researchgate.net/publication/339800429_Discrete_One-
  Dimensional_Signals_A_Brief_Catalogue_of_Features_CDT-23

  """

import numpy as np
import matplotlib.pyplot as plt
import csv

# Primeiro obtemos nosso sinal:

# Lista de arquivos a serem abertos:
file_list = ['split_a.csv', 'split_b.csv','split_c.csv','split_e.csv',
            'split_fg2.csv']

# Arquivo que vamos escrever:
with open('pow_spec.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for f in file_list:

        power_spectrum = []

        # Abrir o arquivo contendo o padrão
        with open(f, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # Depois organizamos os padrões em arrays
            for row in reader:
                split = np.array([int(s) for s in row])

                # Depois obtemos o parâmetro de frequências ( ou bins de frequência )
                freq = np.fft.fftfreq(len(split))

                # Para não termos valores duplicados no negativo (por ser uma função com
                # números imaginários) escolhemos apenas os bins com frequências positivas.
                mask = freq > 0

                # Agora realizamos a FFT usando a função da biblioteca numpy:
                fourier = np.fft.fft(split)
                # Então ajustamos os valores para termos apenas representações positivas
                n_fourier = 2.*abs(fourier/len(split))

                # Finalmente calculamos o espectro de potência
                power_spec = (2.*(abs(fourier/len(split))**2))
                for i in power_spec:
                    power_spectrum.append(i)

        file.writerow(power_spectrum)
