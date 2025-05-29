from consts import *
from random import randint


def F(X):
    """
    Реализация модели, в этой функции нужно найти экстремум
    X: Вектор аргументов
    Выводит значение функции от вектора аргументов
    """
    # цена плана поставок Z
    plane_price = 0
    for n in range(N):
        for i in range(bakery):
            plane_price += (values[i][n]*sum([X[i][n][m] for m in range(M)]))
    plane_price /= a

    # стоимость продажи в n корпусе m пироженного
    sale_values = [[0]*M for n in range(N)]
    for n in range(N):
        for m in range(M):
            aver_price = 0
            for i in range(bakery):
                aver_price += (pur_values[i][m] * X[i][n][m])

            sum_x_i = sum([X[i][n][m] for i in range(bakery)])
            if sum_x_i:
                aver_price /= sum_x_i

            sale_values[n][m] = aver_price * (1 + alpha * (beta**cafes[n]))
            sale_values[n][m] *= (1 - gamma*(sum_x_i - gal[m] * consumers[n]))
            sale_values[n][m] -= aver_price
            sale_values[n][m] *= sum_x_i

    # доход от продаж I
    sales_income = 0
    for n in range(N):
        for m in range(M):
            for i in range(bakery):
                sales_income += sale_values[n][m] * X[i][n][m]

    # ее нужно максимизировать, то есть минимизировать -F
    fun = sales_income - plane_price
    return -fun

def new_x(x):
    """
    Создаёт новое состояние, слегка меняя один случайный элемент x[i][n][m].
    Предполагается, что x — трехмерный список или массив.
    """

    new_state = x.copy()

    # Случайный выбор индексов
    i = randint(0, bakery - 1)
    n = randint(0, N - 1)
    m = randint(0, M - 1)

    # Случайное отклонение
    delta = randint(-5, 5)

    new_value = new_state[i][n][m] + delta
    if new_value < 0:
        new_value = 0
    elif new_value > 1000:
        new_value = 1000

    new_state[i][n][m] = new_value
    return new_state

def print_ans(ans):
    for i in range(len(ans)):
        print(f"Значение функции: {ans[i][0]}")
        print("План поставок (X[i][n][m]):")
        for j in range(len(ans[i][1])):  # по пекарням
            print(f"Пекарня {j+1}:")
            for n in range(len(ans[i][1][j])):  # по корпусам
                row = f"  Корпус {n+1}:"
                for m in range(len(ans[i][1][j][n])):  # по пирожным
                    val = ans[i][1][j][n][m]
                    row += f" {m+1}:{val:5} "
                print(row)