import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Проект FitLife - MVP версия 1.0

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age
# (не забудь преобразовать в число)
user_name = input('Введите Ваше имя: ')

try:
    user_age = int(input('Введите Ваш возраст: '))
except ValueError:
    print('Ошибка: Нужно ввести целое число!')

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
# и сохрани в user_height (тип float)
try:
    user_weight = float(input('Введите Ваш вес в кг: '))
except ValueError:
    print('Ошибка: Нужно ввести число c плавающей точкой!')

try:
    user_height = float(input('Введите Ваш рост в метрах: '))
except ValueError:
    print('Ошибка: Нужно ввести число c плавающей точкой!')

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_needed(user_weight):
    """Вычисляет необходимое количество воды."""
    WATER_PER_KG = 30
    WATER_ML_IN_LITER = 1000

    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / WATER_ML_IN_LITER

    return round(water_l, 1)


water_liters = water_needed(user_weight)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
# TODO: например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_liters:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")
