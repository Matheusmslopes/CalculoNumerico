import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 2, 4, 6, 8, 10])
y = np.array([0, 4, 8, 12, 16, 20])

def TempoPositivo():
    while True:
        Tempo = int(input("Escolha o tempo: "))
        if Tempo >= 0:
            return Tempo
        print("O tempo precisa ser maior ou igual a 0")

def lagrange(x, y):
    def L(i, xi):
        # Calcula o i-ésimo polinômio base de Lagrange no ponto xi
        termos = [(xi - x[j])/(x[i] - x[j]) for j in range(len(x)) if j != i]
        return np.prod(termos)
    def Produto(xi):
        # Calcula o valor do polinômio interpolador no ponto xi
        return sum(y[i] * L(i, xi) for i in range(len(x)))
    
    return Produto

def InterpolacaoPolinomial():
    # Plotando os pontos e o polinômio interpolador
    coef = np.polyfit(x, y, 2)
    polinomio = np.poly1d(coef)
    xp = np.linspace(min(x), max(x), 100)
    plt.plot(xp, polinomio(xp), label='Polinômio Interpolador')
    plt.plot(x, y, '.', label='Pontos')

    # Configurando o gráfico
    plt.title('Polinômio Interpolador de Lagrange')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Mostrando o gráfico
    plt.show()

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

def AjusteCurvas():
    """
    Objetivo: Ajustar uma função linear à relação tempo-velocidade e 
            analisar se a aceleração do carro é constante. 
    Metodologia: Usar o método dos mínimos quadrados para encontrar
            a melhor reta que se ajuste aos dados

    variaveis necessarias:
    n = número de elementos
    somax = é a soma de todos os elementos de x
    somay = é a soma de todos os elementos de y
    somax2 = á soma de cada elemento de x elevado ao quadrado. (EX: x1² + x2² + x3² + ...)
    somaxy = é a soma de cada elemento de x, multiplicado por cada elemento de y; (Ex: (x1 * y1) + (x2 * y2) + (x3 * y3) + ...)
    somaXquadrado = é o quadrado da variavel somax
    """
    n = 6
    somax = 30
    somay = 60
    somax2 = 220
    somaxy = 440
    somaXquadrado = somax * somax

    media_x = somax / n
    media_y = somay / n

    b = ((n * somaxy) - (somax * somay)) / ((n * somax2) - somaXquadrado)

    a = media_y - (b * media_x)

    print(f"a = {a} ")
    print(f"b = {b} ")

    print(f"y = {a} + {b}x")

def main():
    print('Escolha o método:')
    print('Interpolacao Polinomial: 1')
    print('Integração Numérica: 2 ')
    print('Ajuste de Curvas: 3 ')
    print('Método da Bisseção: 4')
    respota = int(input('Digite o valor para escolher o método: '))
   
    if respota == 1: 
       Tempo = TempoPositivo()
       Velocidade = lagrange(x, y)
       VelFinal = Velocidade(Tempo)
       print(f"Velocidade do carro no tempo {Tempo}s: {VelFinal} m/s.")
       InterpolacaoPolinomial()
    elif respota == 2:
        distancia = distanciaTotal(x, y)
        print(f"Distância total: {distancia} metros")       
    elif respota == 3:
        AjusteCurvas()

if __name__ == "__main__":
    main()