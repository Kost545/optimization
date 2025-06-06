N = 8 # корпуса
bakery = 2 # пекарни
cafes = (3, 3, 3, 5, 3, 0, 1, 3) # число кафе вокруг n корпус

# стоимость проезда из i пекарни в n корпус
values = ((210, 209, 220, 337, 210, 215, 180, 195),
          (210, 180, 202, 191, 200, 245, 325, 185))

# студенты и преподаватели n корпуса количество
students = (89, 171, 150, 103, 124, 75, 73, 15)
teachers = (1088, 2352, 2148, 1648, 2776, 464, 1424, 340)

# количество потребителей
consumers = [students[i] + 2*teachers[i] for i in range(N)]

M = 8 # пироженные
# стоимость покупки из i пекарни m пироженного
pur_values = ((100, 100, 155, 135, 25, 180, 300, 200),
              (85, 85, 85, 95, 100, 85, 90, 95))

# желанность m пироженного
gal = (0.6, 0.4, 0.5, 0.8, 1, 0.6, 0.9, 0.8)

# подгоночные параметры для усложнения функции
a = 0.00001
alpha = 0.001
beta = 1.0001
gamma = 0.5

temperature = 1000.0  # Начальная температура
cooling_rate = 0.995 # Скорость охлаждения
min_temperature = 0.00000001
max_iterations = 100000 # Максимальное количество итераций

# научиться решать сложные оптимизационные задачи с помощью алгоритма исскуственного интелекта
# пироженные постановка задачи