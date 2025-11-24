# 1 вариант Andrey Rudz
import json

print("start code ...")
data_json = [{
    "id": 1,
    "name": "Окунь",
    "latin_name": "Perca fluviatilis",
    "is_salt_water_fish": False,
    "sub_type_count": 3
},
    {
        "id": 2,
        "name": "Рыба-черт",
        "latin_name": "Lophius piscatorius",
        "is_salt_water_fish": True,
        "sub_type_count": 5
    },
    {
        "id": 3,
        "name": "Лещ",
        "latin_name": "Abramis brama",
        "is_salt_water_fish": False,
        "sub_type_count": 2
    },
    {
        "id": 4,
        "name": "Рыба-капля",
        "latin_name": "Psychrolutes marcidus",
        "is_salt_water_fish": True,
        "sub_type_count": 1
    },
    {
        "id": 5,
        "name": "Тупорылая акула",
        "latin_name": "Carcharhinus leucas",
        "is_salt_water_fish": True,
        "sub_type_count": 7
    }
]

<<<<<<< HEAD
def Output_all_entries():
    for i in range(len(data)):
                for key in data[i]:
                    print(f'{key} - {data[i][key]}')
                print('-' * 50)
def Output_entry_by_id(choice_id):
    found = False
    for fish in data:
        if fish['id'] == choice_id:
            found = True
            print(f"НАЙДЕНА РЫБА С ID {choice_id}:")
            for key,value in fish.items():
                print(f'{key} - {value}')
            break
    if not found:
        print("Рыбы с таким id нету")
def  Add_entry():
    fields = list(data[0].keys())[1:]
    new_id = max(fish['id'] for fish in data) + 1
    new_fish = {'id': new_id}

    for key in fields:
        value = input(f'{key} : ')
        if key == "is_salt_water_fish":
            value = value.lower() in ('true','yes','да','1')
        elif key == "sub_type_count":
            try:
                value = int(value)
            except ValueError:
                print("Ошибка: введите целое число для количества подтипов")
                return
        new_fish[key] = value
    data.append(new_fish)
    with open('fish.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    print(f"Рыба успешно добавлена с ID:{new_id}")
def Delete_entry_by_id(delete_id):
    found = False
          
    for i,fish in enumerate(data):
        if fish['id'] == delete_id:
            del data[i]
            found = True
            print(f"Рыба с ID {delete_id} удалена")
            break
        if not found:
            print("Рыбы с таким ID нету")
        with open('fish.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
=======
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed

with open("fish.json", 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=4, ensure_ascii=False)

with open('fish.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
choice = 0
while choice != 5:
<<<<<<< HEAD
=======
    len_data = len(data)
    fields = list(data[0].keys())[1:]


>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed

    try:
        choice = int(input('''
МЕНЮ:
1) Вывести все записи
2) Вывести запись по полю
3) Добавить запись
4) Удалить запись по ID
5) Выйти из программы

Ваш выбор: '''))

        if choice == 1:

            print("ВСЕ ЗАПИСИ:")
<<<<<<< HEAD
            Output_all_entries()
=======
            for i in range(len(data)):
                for key in data[i]:
                    print(f'{key} - {data[i][key]}')
                print('-' * 50)
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed

        elif choice == 2:
            try:

                choice_id = int(input("Введите ID рыбы: "))
<<<<<<< HEAD
                Output_entry_by_id(choice_id)
=======
                found = False
                for fish in data:
                    if fish['id'] == choice_id:
                        found = True
                        print(f"НАЙДЕНА РЫБА С ID {choice_id}:")
                        for key,value in fish.items():
                            print(f'{key} - {value}')
                        break
                if not found:
                    print("Рыбы с таким id нету")
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed
            except ValueError:
                print("Ошибка: введите корректный номер")
        elif choice == 3:
            print("ДОБАВЛЕНИЕ НОВОЙ РЫБЫ:")
            try:
<<<<<<< HEAD
                Add_entry()   
=======

                new_id = max(fish['id'] for fish in data) + 1
                new_fish = {'id': new_id}

                for key in fields:
                    value = input(f'{key} : ')
                    if key == "is_salt_water_fish":
                        value = value.lower() in ('true','yes','да','1')
                    elif key == "sub_type_count":
                        value = int(value)

                    new_fish[key] = value

                data.append(new_fish)
                with open('fish.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file)

                print(f"Рыба успешно добавлена с ID:{new_id}")
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed
            except ValueError:
                print("Ошибка: введите корректный номер")
        elif choice == 4:
            try:
<<<<<<< HEAD
                delete_id = int(input("Введите ID рыбы для удаление:"))
                Delete_entry_by_id(delete_id)
=======
                found = False
                delete_id = int(input("Введите ID рыбы для удаление:"))
                for i,fish in enumerate(data):
                    if fish['id'] == delete_id:
                        del data[i]
                        found = True
                        print(f"Рыба с ID {delete_id} удалена")
                        break
                if not found:
                    print("Рыбы с таким ID нету")
                with open('fish.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed

            except ValueError:
                print("Ошибка: введите корректный номер")
        elif choice == 5:
            print("Выход из программы...")
        else:
            print("Неверный выбор! Введите число от 1 до 5")

    except ValueError:
        print("Ошибка: введите корректный номер")
    id_fish = []

<<<<<<< HEAD
print("end code")
=======
print("end code")
>>>>>>> 8a94d00160da5aeffdf8125753f188d9cd8a3fed
