import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10])
y = np.array([0, 4, 8, 12, 16, 20])

def distanciaTotal(x, y):
    h = x[1] - x[0]
    area_trapezios = h * np.sum((y[:-1] + y[1:]) / 2)
    area_primeiro_ultimo = (h/2) * (y[0] + y[-1]) /2
    distancia = area_trapezios + area_primeiro_ultimo
    return distancia

def distanciaAcumulada(x, y):
    h = x[1] - x[0]
    dist_acumulada = [0]  # Inicia com 0 no tempo 0
    for i in range(1, len(x)):
        area_trapezio = h * (y[i-1] + y[i]) / 2
        dist_acumulada.append(dist_acumulada[-1] + area_trapezio)
    return np.array(dist_acumulada)



# Calcula a distância total e a distância acumulada
distancia = distanciaTotal(x, y)
dist_acumulada = distanciaAcumulada(x, y)
print(f"Distância total: {distancia} metros")

# Cria o gráfico de velocidade versus tempo e distância acumulada
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Velocidade (m/s)')
plt.plot(x, dist_acumulada, marker='x', linestyle='--', color='r', label='Distância Acumulada (m)')
plt.title('Gráfico de Velocidade vs Tempo e Distância Acumulada')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s) e Distância (m)')
plt.grid(True)
plt.legend()
plt.show()

# plt.figure(figsize=(10, 5))
# plt.plot(x, y, marker='o', linestyle='-', color='b', label='Velocidade (m/s)')
# plt.plot(x, dist_acumulada, marker='x', linestyle='--', color='r', label='Distância Acumulada (m)')
# plt.title('Gráfico de Distância vs Tempo')
# plt.xlabel('Tempo (s)')
# plt.ylabel('Distância (m)')
# plt.grid(True)
# plt.legend()
# plt.show()

