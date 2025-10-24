#1 вариант Andrey Rudz
import json

found = False
with open("dump.json","r",encoding='utf-8') as file:
    info_from_file = json.load(file)

special = input("Введите код специальности")

for info in info_from_file:
    if info['model'] == 'data.specialty' and info['fields']["code"] == special:
        specialty_info = info['pk']
        
        for skill in info_from_file:
            if skill['model'] == 'data.skill' and skill['pk'] == specialty_info:
                print(f'''
=============== Найдено ===============
{info['fields']["code"]} >> Специальность "{info['fields']["title"]}", {info['fields']["c_type"]}
{skill['fields']["code"]} >> Квалификация "{skill['fields']["title"]}"
''')
                found = True
                break
        break

if not found:
    print('=============== Не найдено ===============')