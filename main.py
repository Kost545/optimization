from simulated_annealing import *
from function import *
from consts import *
import matplotlib.pyplot as plt
import numpy as np

# нужно установить matplotlib и numpy

ans = []
initial_state = np.random.randint(0, 1000, size = (bakery, N, M))  # Начальная точка

# запуски метода оптимизации
for i in range(10):
    best_state, best_value, values = simulated_annealing(F, initial_state, temperature)

    ans.append((-best_value, best_state, values))

# вывод лучших значений и лучших векторов аргументов
print_ans(ans)

# Генерация цветов
colors = plt.cm.viridis(np.linspace(0, 1, len(ans)))
# Создание точечного графика
for i in range(len(ans)):
    x = range(len(ans[i][2]))
    y = ans[i][2]

    # Рисуем график с тонкой линией и уникальным цветом
    plt.plot(x, y,
             color=colors[i],
             marker='o',
             markersize=1,  # уменьшаем размер маркеров
             linewidth=0.1,  # очень тонкая линия
             alpha=0.7)  # добавляем подпись для легенды

# Настройки графика
plt.title('Значения функции с разными запусками метода отжига')
plt.xlabel('Итерация')
plt.ylabel('Значение')
plt.grid(True, linestyle=':', linewidth=0.5)  # делаем сетку пунктирной и тонкой

# Улучшаем внешний вид
plt.tight_layout()  # автоматическая подгонка отступов
plt.show()

