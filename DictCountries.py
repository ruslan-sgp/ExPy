import pickle
import json

# Изначальный словарь стран и столиц
countries = {
    "Россия": "Москва",
    "Германия": "Берлин",
    "Франция": "Париж"
}

# Функция для добавления страны и столицы
def add_country(country, capital):
    countries[country] = capital

# Функция для удаления страны
def delete_country(country):
    if country in countries:
        del countries[country]
    else:
        print(f"Страна {country} не найдена")

# Функция для поиска столицы по стране
def search_country(country):
    return countries.get(country, f"Страна {country} не найдена")

# Функция для редактирования данных о столице
def edit_country(country, new_capital):
    if country in countries:
        countries[country] = new_capital
    else:
        print(f"Страна {country} не найдена")

# Функция для сохранения данных в файл (с разными форматами)
def save_data(filename, format="pickle"):
    if format == "binary":
        with open(filename, 'wb') as file:
            file.write(str(countries).encode())  # Сохранение как бинарный поток
    elif format == "text":
        with open(filename, 'w', encoding='utf-8') as file:
            for country, capital in countries.items():
                file.write(f"{country}:{capital}\n")  # Сохранение как текстовый поток
    elif format == "pickle":
        with open(filename, 'wb') as file:
            pickle.dump(countries, file)  # Сохранение с использованием pickle
    elif format == "json":
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(countries, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON
    else:
        print("Неверный формат")

# Функция для загрузки данных из файла (с разными форматами)
def load_data(filename, format="pickle"):
    global countries
    try:
        if format == "binary":
            with open(filename, 'rb') as file:
                countries = eval(file.read().decode())  # Чтение как бинарный поток
        elif format == "text":
            with open(filename, 'r', encoding='utf-8') as file:
                countries = {}
                for line in file:
                    country, capital = line.strip().split(":")
                    countries[country] = capital  # Чтение как текстовый поток
        elif format == "pickle":
            with open(filename, 'rb') as file:
                countries = pickle.load(file)  # Чтение с использованием pickle
        elif format == "json":
            with open(filename, 'r', encoding='utf-8') as file:
                countries = json.load(file)  # Чтение из JSON
        else:
            print("Неверный формат")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except (pickle.UnpicklingError, json.JSONDecodeError, ValueError) as e:
        print(f"Ошибка при загрузке данных: {e}")

# Пример использования

print('Начальный словарь:')
print('\t', countries)

add_country("Италия", "Рим")
print('После добавления:')
print('\t', countries)

edit_country("Франция", "Лион")
print('После редактирования:')
print('\t', countries)

print('Поиск столицы России:')
print('\t', search_country("Россия"))  # "Москва"

delete_country("Германия")
print('После удаления:')
print('\t', countries)

# Сохранение и загрузка в разных форматах

# Pickle
save_data("countries.pkl", "pickle")
load_data("countries.pkl", "pickle")
print('После сохранения и загрузки через pickle:')
print('\t', countries)

# JSON
save_data("countries.json", "json")
load_data("countries.json", "json")
print('После сохранения и загрузки через JSON:')
print('\t', countries)

# Бинарный поток
save_data("countries.bin", "binary")
load_data("countries.bin", "binary")
print('После сохранения и загрузки через бинарный поток:')
print('\t', countries)

# Текстовый поток
save_data("countries.txt", "text")
load_data("countries.txt", "text")
print('После сохранения и загрузки через текстовый поток:')
print('\t', countries)
