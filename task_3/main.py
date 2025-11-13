#1 вариант Andrey Rudz
import json
print("start code ...")
data_json = [    {
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
with open("fish.json",'w', encoding='utf-8') as file:
    json.dump(data_json,file,indent=4, ensure_ascii=False)

with open ('fish.json','r',encoding='utf-8') as file:
    data = json.load(file)
choice = 0
while choice != 5:
    len_data = len(data)
    id_fish = []
    fields = [data[0].keys]
    for i in range(len_data):
        id_fish.append(i)

    

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
            for i in range(len(data)):
                for key in data[i]:
                    print(f'{key} - {data[i][key]}')
                print('-'*50)
               
        elif choice == 2:
            try:
                
                choice_id = int(input("Введите id рыбы информацию про которую хотите узнать"))
                if choice_id in id_fish:
                    for key in data[choice_id-1]:
                        print(f'{key} - {data[choice_id-1][key]}')
                   
                else:
                    print("Рыбы с таким id нету")
            except ValueError:
                print("Ошибка: введите корректный номер")
        elif choice == 3:
            try:
                
                
                new_id = len_data + 1
                new_fish  = {'id':new_id}
               
                for key in fields[1:]:
                    value = input(f'{key} : ')
                    data[new_id][key] = value

            except ValueError:
                print("Ошибка: введите корректный номер")
        elif choice == 4:
            pass
        elif choice == 5:
            print("Выход из программы...")
        else:
            print("Неверный выбор! Введите число от 1 до 5")
            
    except ValueError:
        print("Ошибка: введите корректный номер")
    id_fish=[]


print("end code")
