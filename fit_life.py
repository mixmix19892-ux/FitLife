import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Проект FitLife - MVP версия 1.0

user_name = input('Введите Ваше имя: ')

try:
    user_age = int(input('Введите Ваш возраст: '))
except ValueError:
    print('Ошибка: Нужно ввести целое число!')


try:
    user_weight = float(input('Введите Ваш вес в кг (например, 50.1): '))
except ValueError:
    print('Ошибка: Нужно ввести число c плавающей точкой!')

try:
    user_height = float(input('Введите Ваш рост в метрах: '))
except ValueError:
    print('Ошибка: Нужно ввести число c плавающей точкой!')

bmi = round(user_weight / (user_height ** 2), 1)


def water_needed(user_weight):
    """Вычисляет необходимое количество воды."""
    WATER_PER_KG = 30
    WATER_ML_IN_LITER = 1000

    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / WATER_ML_IN_LITER

    return round(water_l, 1)


water_liters = water_needed(user_weight)

print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_liters:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")
