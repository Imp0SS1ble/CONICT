import matplotlib.pyplot as plt # Incluindo a biblioteca matplotlib.pyplot e dando o apelido de plt.
from scipy.optimize import curve_fit # Incluindo a biblioteca scipy.optimize.
import numpy as np # Incluindo a biblioteca numpy e dando o apelido de np.
t = []
t = [] # Declarando o vertor que será usado no código.
x = [0.0] # Definindo a posição do primeiro sensor como a origem.
n = int(input('Informe quantos sensores foram usados: '))# Pedindo para o usuário informar quantos sensores foram usados.
t = np.array([float(input('Informe quantos segundos deu no ' +str(i+1)+'º sensor (em segundos): ')) for i in range(n)]) # Pedindo para o usuário informar os tempos medido pelo cronômetro em cada sensor.
for i in range(n-1, -1, -1): t[i] = t[i] - t[0] # Calculando o tempo medido dos sensores em relação ao primeiro sensor.
for i in range(1, n):
   x.append(float(input('Informe a distância do ' +str(1)+'º ao '+str(i+1)+'º sensor (em metros): '))) #Pedindo para o usuário informar as distâncias dos sensores em relação ao primeiro sensor.
def y(t, C, v0, x0): # Criando a função com a equação do movimento retilíneo uniforme.
    return  (C*t**2) + v0*t + x0
xData = np.array(t) # Colocando as variáveis de tempo nos dados do exo x.
yData = np.array(x) # Colocando as variáveis de posição nos dados do exo y.
fig, ax = plt.subplots(figsize = (8,5)) # Definindo o tamanho do gráfico para melhor visualização.
plt.axis(ymin=0, ymax=(x[n-1])*1.1, xmin=0, xmax=(t[n-1])*1.1) # Definindo os valores limites dos eixos do gráfico.
plt.title('Movimento retilíneo com aceleração constante') # Título do gráfico.
plt.plot(xData, yData, 'bo', label='Dados') # Plotando valores informados pelo usuário.
popt, pcov = curve_fit(y, xData, yData) # Calculando parâmetros fixos por meio da função da linha X.
xFit = np.arange(0.0, t[n-1], 0.000001) # Definindo o tamanho e o intervalo da curva de tendência.
plt.plot(xFit, y(xFit, *popt), 'r', label=f'Parâmetros fixos de ajuste:\n C={popt[0]:.6} m/s**2, v0={popt[1]:.5} m/s, x0={popt[2]:.5e} m\nEquação: x = C*t**2 + v0*t + x0') # Plotando valores calculados no ajuste de curva.
plt.xlabel('t (s)') # Título da eixo x.
plt.ylabel('x (m)') # Título da eixo y.
plt.legend() # Exibição da legenda.
plt.show() # Exibição do gráfico.
