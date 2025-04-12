from math import exp
from random import random
from function import new_x
from consts import cooling_rate, min_temperature, max_iterations


def simulated_annealing(func, initial_state, temperature):
    """
    Реализация метода отжига для минимизации функции.

    func: Функция, которую нужно минимизировать.
    initial_state: Начальное состояние (начальная точка).
    temperature: Начальная температура.
    cooling_rate: Скорость охлаждения (температура уменьшается на этот коэффициент на каждом шаге).
    max_iterations: Максимальное количество итераций.
    Выводит лучшее найденное состояние и значение функции в этом состоянии.
    """
    current_state = initial_state
    current_value = func(current_state)
    best_state = current_state
    best_value = current_value
    iteration = 0
    values = []

    while temperature > min_temperature or iteration < max_iterations:
        # Генерация нового состояния
        new_state = new_x(current_state)
        new_value = func(new_state)

        # Вычисление разницы значений функции
        delta = new_value - current_value

        # Если новое состояние лучше, принимаем его
        if delta <= 0:
            current_state, current_value = new_state, new_value
            if new_value < best_value:
                best_state, best_value = new_state, new_value
        else:
            # Иначе принимаем новое состояние с вероятностью exp(delta / temperature)
            probability = exp(-delta / temperature)
            if random() < probability:
                current_state, current_value = new_state, new_value

        # Охлаждение
        temperature *= cooling_rate
        iteration += 1
        values.append(-current_value)

    return best_state, best_value, values

