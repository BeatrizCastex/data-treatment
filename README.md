Projeto 2 - Análise e Reconhecimento de Padrões
Beatriz de Camargo Castex Ferreira - 10728077
Docente: Prof. Luciano da Fontoura Costa
USP São Carlos - IFSC
05/2020

OS ARQUIVOS DESSA PASTA FORAM FEITOS COM OBJETIVOS EDUCATIVOS COMO PARTE DE UM
PROJETO DA MATÉRIA DE ANÁLISE E RECONHECIMENTO DE PADRÕES DO CURSO DE GRADUAÇÃO
EM FÍSICA COMPUTACIONAL DO IFSC-USP.

Os padrões de autônomos foram gerados através dos códigos do projeto 1 da mesma matéria.
Mais informações e referências no relatório do projeto incluso.


===== Descrição do projeto =====

Implementar 4 dos seguintes conjuntos de medidas e testar sobre sinais gerados
por autômatos probabilíssimos como os já vistos em aula, incluindo o autômato
da Figura 2 do CDT-23:
1. Média, desvio padrão, entropia e evenness do
número de bursts, e respectivos tamanhos nos split signals;
2. Média, desvio padrão, entropia e evenness do
número de distâncias intersímbolos e respectivos valores nos split signals;
3. Média e desvio padrão das magnitudes do espectro de potência da transformada
de Fourier discreta dos split signals (pode usar rotina Para FFT);
4. Média e desvio do grau e coeficiente de aglomeração de grafos dos sinais,
obtidos pelo método de visibilidade, que deve ser implementado;
5. Coeficiente alpha do DFA da integral do sinal.

=================================

=========== ÍNDICE ==============

1-figuras:
   Pasta contendo todas as imagens e gráficos geradas na produção do projeto.

2-split:
  Programas para fazer os padrões split signals;

  1-single:
    Programa para fazer split signal dos padrões gerados por um único autômato;
    Arquivos com padrões utilizados para gerar split signals usados para fazer as figuras;

  2-multiple:
    Programa para fazer split signal de padrões gerados por muitos autômatos;
    Arquivos com padrões utilizados para gerar split signals usados nos programas após esse.

3-burst:
  Programa que análisa padrões split signals para achar bursts
  Arquivos com os split signals utilizados para gerar os dados utilizados no projeto.

4-interdistance:
  Programa que análisa padrões split signals para achar distâncias intersímbolos.
  Arquivos com os split signals utilizados para gerar os dados utilizados no projeto.

5-fourier:
  fourier_ps: Programa que faz o gráfico de espectro de potência da FFT de um sinal.
  power_spectrum: Programa que calcula os espectros de potências das FFTs de vários sinais.
  Arquivos com os split signals utilizados para gerar os dados utilizados no projeto.


6-statistics:
  Programa que calcula o desvio padrão, média, densidade de probabilidade normal de conjuntos de dados.
  Arquivos utilizados para gerar os valores apresentados no projeto.

7-visibility:
  Programa que implementa o método de visibilidade para formação de grafos e calcula grau e coeficiente de aglomeração
  Arquivos utilizados para gerar os valores apresentados no projeto.

aut-fg2 :
  Programa usado para criar padrões usando o autômato do CDT-23.

