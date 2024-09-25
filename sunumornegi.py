import numpy as np

def fitness_function(parameters):
    # Redüktörün ağırlığını hesapla (tasarım parametrelerine bağlı)
    # Örneğin: ağırlık = w1 * p1 + w2 * p2 + ...
    # Burada tasarım parametrelerini kullanarak ağırlığı hesaplayın
    # Daha karmaşık bir modeliniz varsa bu fonksiyonu uygun şekilde güncelleyin
    # Örneğin, gerilim sınırları, yüzey gerilimleri, şaft eğilmesi vb. dikkate alınabilir
    # Ağırlığı minimize etmek için uygun bir formül kullanın
    # Döndürülen değer daha düşük olmalıdır (minimize edilmelidir)

    # Örnek olarak:
    weight = np.dot(parameters, weights)

    return weight

def hho_optimization(dim, n, max_iter):
    X = np.random.rand(n, dim)  # Başlangıç konumları
    best_fitness = float('inf')
    best_solution = np.zeros(dim)
    for t in range(max_iter):
        for i in range(n):
            fitness = fitness_function(X[i])
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = X[i]
            # Harris Hawks'ın hareketi
            E0 = 2 * np.random.rand() - 1
            E1 = 2 * np.random.rand() - 1
            E2 = 2 * np.random.rand() - 1
            # Konum güncellemesi
            X[i] = X[i] + E0 * (X[i] - best_solution) + E1 * (X[i] - X[np.random.randint(0, n)]) + E2 * (X[np.random.randint(0, n)] - X[np.random.randint(0, n)])
            # Sınırları kontrol et
            X[i] = np.clip(X[i], 0, 1)  # Örneğin, 0 ile 1 arasında sınırla
    return best_solution, best_fitness

# Ağırlıkları normalize et
dim = 5  # Tasarım parametre sayısı
weights = np.random.rand(dim)
weights /= np.sum(weights)

# Örnek kullanım
# dim = 15
n = 100   # Kuş sayısı
max_iter = 20

best_solution, best_fitness = hho_optimization(dim, n, max_iter)
print("En iyi çözüm:", best_solution)
print("En iyi uygunluk değeri:", best_fitness)
print("Ağırlıklar:", weights)
