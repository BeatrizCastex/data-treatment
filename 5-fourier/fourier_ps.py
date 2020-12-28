""" ESPECTRO DE POTÊNCIA E FFT
  Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
  05/2020

  Esse programa tem como objetivo fazer uma transformada de fourier em um
  split signal e através disso calcular seu espectro de potência.

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

# Primeiro obtemos nosso sinal:
split = [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
1, 0, 0, 0, 1, 0, 0, 1, 0, 1] # Esse padrão é um placeholder

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
power_spectrum = 2.*(abs(fourier/len(split))**2)


# Plotando o espectro de potência
fig, ax= plt.subplots(figsize=(9,3))
ax.stem(freq[mask], power_spectrum[mask], use_line_collection=True)
plt.xlabel('Frequências')
plt.ylabel('Potência')
plt.title('Espectro de potência')
plt.tight_layout()
plt.show()

# Plotando a transformada de Fourier
plt.plot(freq[mask], n_fourier[mask])
plt.title('Transformada de Fourier')
plt.show()
