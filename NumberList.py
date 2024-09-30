# Изначально пустой список для хранения чисел
numbers = []

# Функция для отображения меню
def show_menu():
    print("\nМеню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить наличие числа в списке")
    print("5. Заменить значение в списке")
    print("6. Выйти")

# Функция для добавления нового числа
def add_number():
    try:
        number = int(input("Введите число для добавления: "))
        if number in numbers:
            print(f"Число {number} уже существует в списке.")
        else:
            numbers.append(number)
            print(f"Число {number} добавлено в список.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Функция для удаления всех вхождений числа
def delete_number():
    try:
        number = int(input("Введите число для удаления: "))
        if number in numbers:
            numbers[:] = [x for x in numbers if x != number]
            print(f"Все вхождения числа {number} удалены.")
        else:
            print(f"Число {number} не найдено в списке.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Функция для показа содержимого списка
def show_list():
    if len(numbers) == 0:
        print("Список пуст.")
    else:
        order = input("Показать список с начала или с конца? (введите 'с начала' или 'с конца'): ").strip().lower()
        if order == 'с начала':
            print("Список с начала:", numbers)
        elif order == 'с конца':
            print("Список с конца:", list(reversed(numbers)))
        else:
            print("Неверный выбор.")

# Функция для проверки наличия числа в списке
def check_number():
    try:
        number = int(input("Введите число для поиска: "))
        if number in numbers:
            print(f"Число {number} найдено в списке.")
        else:
            print(f"Число {number} отсутствует в списке.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Функция для замены числа в списке
def replace_number():
    try:
        old_number = int(input("Введите число для замены: "))
        if old_number not in numbers:
            print(f"Число {old_number} отсутствует в списке.")
            return
        
        new_number = int(input("Введите новое число: "))
        replace_all = input("Заменить все вхождения? (да/нет): ").strip().lower()

        if replace_all == "да":
            numbers[:] = [new_number if x == old_number else x for x in numbers]
            print(f"Все вхождения числа {old_number} заменены на {new_number}.")
        elif replace_all == "нет":
            index = numbers.index(old_number)
            numbers[index] = new_number
            print(f"Первое вхождение числа {old_number} заменено на {new_number}.")
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Пожалуйста, введите целое число.")
    except IndexError:
        print(f"Число {old_number} не найдено.")

# Основной цикл программы
while True:
    show_menu()
    choice = input("Выберите действие (1-6): ").strip()

    if choice == "1":
        add_number()
    elif choice == "2":
        delete_number()
    elif choice == "3":
        show_list()
    elif choice == "4":
        check_number()
    elif choice == "5":
        replace_number()
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт из меню.")
