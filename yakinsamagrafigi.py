import numpy as np
import matplotlib.pyplot as plt

def hho(objective_function, lb, ub, dim, n, max_iter):
    # Parametreler ve başlangıç değerleri
    X = np.random.rand(n, dim) * (ub - lb) + lb
    fitness = np.zeros(n)
    best_fitness = float('inf')
    best_solution = np.zeros(dim)
    fitness_values = []  # Uygunluk değerlerini saklamak için boş bir dizi

    for t in range(max_iter):
        # Fitness değerlerini hesapla
        for i in range(n):
            fitness[i] = objective_function(X[i])

            if fitness[i] < best_fitness:
                best_fitness = fitness[i]
                best_solution = X[i]

        # Harris Hawks'ın hareketi
        for i in range(n):
            E0 = 2 * np.random.rand() - 1
            E1 = 2 * np.random.rand() - 1
            E2 = 2 * np.random.rand() - 1

            X[i] = X[i] + E0 * (X[i] - best_solution) + E1 * (X[i] - X[np.random.randint(0, n)]) + E2 * (X[np.random.randint(0, n)] - X[np.random.randint(0, n)])

            # Sınırları kontrol et
            X[i] = np.clip(X[i], lb, ub)

        # Her iterasyonda en iyi uygunluk değerini sakla
        fitness_values.append(best_fitness)

    # Uygunluk değerlerini grafiğe çizin
    plt.plot(fitness_values)
    plt.xlabel("Iterasyon Sayısı")
    plt.ylabel("Uygunluk Değeri")
    plt.title("HHO Algoritması Yakınsama Grafiği")
    plt.grid(True)
    plt.show()

    return best_solution, best_fitness

# Örnek kullanım
def sphere(x):
    return np.sum(x**2)

lb = -10  # Alt sınırlar
ub = 10   # Üst sınırlar
dim = 10  # Boyut
n = 20    # Kuş sayısı
max_iter = 100 

best_solution, best_fitness = hho(sphere, lb, ub, dim, n, max_iter)
print("En iyi çözüm:", best_solution)
print("En iyi uygunluk değeri:", best_fitness)
