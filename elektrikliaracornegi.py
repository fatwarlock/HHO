import numpy as np

def energy_balance_optimization(ev_arrival_rate, grid_supply_rate, max_iter=150):
    # Parametreler ve başlangıç değerleri
    n = len(ev_arrival_rate)  # Elektrikli araç sayısı
    dim = n  # Boyut (her araç için bir boyut)
    X = np.random.rand(n, dim) * (grid_supply_rate / 2)  # Başlangıç konumları
    fitness = np.zeros(n)
    best_fitness = float('inf')
    best_solution = np.zeros(dim)

    for t in range(max_iter):
        # Fitness değerlerini hesapla
        for i in range(n):
            # Elektrikli araçların şebekeye bağlanma hızını optimize etmek için uygunluk fonksiyonu
            fitness[i] = np.abs(ev_arrival_rate[i] - grid_supply_rate)

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
            X[i] = np.clip(X[i], 0, grid_supply_rate)

    return best_solution

# Örnek kullanım
ev_arrival_rate = [10, 15, 20]  # Elektrikli araçların saatlik bağlanma hızı
grid_supply_rate = 100  # Şebeke tarafından sağlanan saatlik enerji hızı

best_solution = energy_balance_optimization(ev_arrival_rate, grid_supply_rate)
print("En iyi çözüm:", best_solution)
