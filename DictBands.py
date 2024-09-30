import pickle

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

# Функция для сохранения данных в файл с использованием pickle
def save_data(filename):
    with open(filename, 'wb') as file:
        pickle.dump(music_bands, file)

# Функция для загрузки данных из файла с использованием pickle
def load_data(filename):
    global music_bands
    try:
        with open(filename, 'rb') as file:
            music_bands = pickle.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except pickle.UnpicklingError:
        print("Ошибка при загрузке данных из файла")

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

save_data("music_bands.pkl")
load_data("music_bands.pkl")
print('После сохранения pickle и считывания:')
print('\t', music_bands)
