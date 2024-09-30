import pickle
import json

# Изначальный словарь групп и их альбомов
music_bands = {
    "The Beatles": ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"],
    "Pink Floyd": ["The Dark Side of the Moon", "The Wall"],
    "Led Zeppelin": ["Led Zeppelin IV", "Physical Graffiti"]
}

# Функция для добавления группы и альбомов
def add_band(band, albums):
    if band in music_bands:
        music_bands[band].extend(albums)
    else:
        music_bands[band] = albums

# Функция для удаления группы
def delete_band(band):
    if band in music_bands:
        del music_bands[band]
    else:
        print(f"Группа {band} не найдена")

# Функция для поиска альбомов по названию группы
def search_band(band):
    return music_bands.get(band, f"Группа {band} не найдена")

# Функция для редактирования альбомов группы
def edit_band(band, new_albums):
    if band in music_bands:
        music_bands[band] = new_albums
    else:
        print(f"Группа {band} не найдена")

# Функция для сохранения данных в файл (с разными форматами)
def save_data(filename, format="pickle"):
    if format == "binary":
        with open(filename, 'wb') as file:
            file.write(str(music_bands).encode())  # Сохранение как бинарный поток
    elif format == "text":
        with open(filename, 'w', encoding='utf-8') as file:
            for band, albums in music_bands.items():
                file.write(f"{band}:{','.join(albums)}\n")  # Сохранение как текстовый поток
    elif format == "pickle":
        with open(filename, 'wb') as file:
            pickle.dump(music_bands, file)  # Сохранение с использованием pickle
    elif format == "json":
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(music_bands, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON
    else:
        print("Неверный формат")

# Функция для загрузки данных из файла (с разными форматами)
def load_data(filename, format="pickle"):
    global music_bands
    try:
        if format == "binary":
            with open(filename, 'rb') as file:
                music_bands = eval(file.read().decode())  # Чтение как бинарный поток
        elif format == "text":
            with open(filename, 'r', encoding='utf-8') as file:
                music_bands = {}
                for line in file:
                    band, albums = line.strip().split(":")
                    music_bands[band] = albums.split(",")  # Чтение как текстовый поток
        elif format == "pickle":
            with open(filename, 'rb') as file:
                music_bands = pickle.load(file)  # Чтение с использованием pickle
        elif format == "json":
            with open(filename, 'r', encoding='utf-8') as file:
                music_bands = json.load(file)  # Чтение из JSON
        else:
            print("Неверный формат")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except (pickle.UnpicklingError, json.JSONDecodeError, ValueError) as e:
        print(f"Ошибка при загрузке данных: {e}")

# Пример использования

print('Начальный словарь:')
print('\t', music_bands)

add_band("Queen", ["A Night at the Opera", "The Game"])
print('После добавления:')
print('\t', music_bands)

edit_band("Pink Floyd", ["Wish You Were Here", "Animals"])
print('После редактирования:')
print('\t', music_bands)

print('Поиск The Beatles:')
print('\t', search_band("The Beatles"))  # ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"]

delete_band("Led Zeppelin")
print('После удаления:')
print('\t', music_bands)

# Сохранение и загрузка в разных форматах

# Pickle
save_data("music_bands.pkl", "pickle")
load_data("music_bands.pkl", "pickle")
print('После сохранения и загрузки через pickle:')
print('\t', music_bands)

# JSON
save_data("music_bands.json", "json")
load_data("music_bands.json", "json")
print('После сохранения и загрузки через JSON:')
print('\t', music_bands)

# Бинарный поток
save_data("music_bands.bin", "binary")
load_data("music_bands.bin", "binary")
print('После сохранения и загрузки через бинарный поток:')
print('\t', music_bands)

# Текстовый поток
save_data("music_bands.txt", "text")
load_data("music_bands.txt", "text")
print('После сохранения и загрузки через текстовый поток:')
print('\т', music_bands)
