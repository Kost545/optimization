from consts import *
from random import randint
from numpy import random


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
                aver_price += (pur_values[i][m]*X[i][n][m])

            sum_x_i = sum([X[i][n][m] for i in range(bakery)])
            if sum_x_i:
                aver_price /= sum_x_i

            sale_values[n][m] = aver_price * (1 + alpha*(beta**cafes[n]))
            sale_values[n][m] *= (1 - gamma*(sum_x_i - gal[m] * consumers[n]))
            sale_values[n][m] -= aver_price
            sale_values[n][m] *= sum_x_i

    # доход от продаж I
    sales_income = 0
    for n in range(N):
        for m in range(M):
            for i in range(bakery):
                sales_income += sale_values[n][m]*X[i][n][m]*consumers[n]

    # ее нужно максимизировать, то есть минимизировать -F
    fun = sales_income - plane_price - sales_income
    return -fun

def new_x(x):
    # Создает новый вектор аргументов, откланяясь на маленькое значение
    for n in range(N):
        for m in range(M):
            for i in range(bakery):
                new_corr = randint(-1, 1)
                if x[i][n][m] + new_corr > 0:
                    x[i][n][m] += new_corr
                else:
                    x[i][n][m] += new_corr + 1
    return x

def print_ans(ans):
    for i in range(len(ans)):
        print(ans[i][0])

        for j in ans[i][1]:
            for k in j:
                print(*k)
