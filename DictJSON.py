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

# Функция для сохранения данных в файл
def save_data(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(countries, file, ensure_ascii=False, indent=4)

# Функция для загрузки данных из файла
def load_data(filename):
    global countries
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries = json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

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


save_data("countries.json")
load_data("countries.json")
print('После сохранения в JSON и считывания:')
print('\t', countries)
