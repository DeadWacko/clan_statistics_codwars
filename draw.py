import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.colors as mcolors


# Данные
dates = [f"{i}.06.23" for i in range(0, 31)]
users = ['DeadWacko', 'sovosof', 'katelarionova2058']
activity = {
    'DeadWacko': [random.randint(0, 25) for _ in range(31)],
    'sovosof': [random.randint(0, 25) for _ in range(31)],
    'katelarionova2058': [random.randint(0, 25) for _ in range(31)]
}

# Построение графика
plt.figure(figsize=(8, 6))

for user in users:
    plt.plot(dates, activity[user], marker='', label=user)

    # Вычисление линии тренда
    trend_x = np.arange(len(dates))
    trend_y = np.poly1d(np.polyfit(trend_x, activity[user], 1))(trend_x)

    # Определение цвета для линии тренда
    line_color = plt.gca().lines[-1].get_color()  # Получение цвета последней нарисованной линии
    trend_color = mcolors.to_rgb(line_color)  # Преобразование цвета в RGB-формат
    trend_color = tuple([c * 0.7 for c in trend_color])  # Уменьшение яркости цвета

    # Построение линии тренда
    plt.plot(dates, trend_y, color=trend_color, linestyle='--')

    # Добавление горизонтальных линий
    plt.axhline(y=7, color='black', linestyle='-', linewidth=2)
    plt.axhline(y=15, color='black', linestyle='-', linewidth=2)

plt.xlabel('Дата')
plt.ylabel('Количество решенных задач')
plt.title('График активности пользователей')
plt.legend()
plt.grid(True)
plt.xticks(rotation=90)

plt.show()
