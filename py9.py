import collections
'''
from tracemalloc import stop
#Задание 1

def fac(x):
    count = 1
    for i in range(1, x+1):
        count *= i 
    return count

x = int(input())
print(fac(x))

y = []

for i in range(fac(x), 0, -1):
    y.append(fac(i))

print(y)
print('_________________________________________')
'''
# Задание 2

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if 4 < age < 21:
            return 'лет'
    else:
        i = age % 10
        if i==1:
            return 'год'
        elif i < 5:
            return 'года'
        else:
            return 'лет'

def pets_list(pets):
    pets = dict(sorted(pets.items()))
    for i, name in pets.items():
        print(f'\nID животного: {i}')
        for a_name, a_info in name.items():
            print(f'Имя животного: {a_name}')
            print(f'Вид питомца: {a_info['type']}')
            print(f'Возраст животного: {(a_info['age'])}')
            print(f'Имя владельца: {a_info['owner_name']}')

def create():
    x = 1
    last = collections.deque(pets, maxlen=1)
    while (x in pets.keys()):
        x += 1
    last.append(x)
    pets[int(last[0])] = {input('Введите имя животного: '): 
                          {'type': input('Введите тип животного: '), 
                           'age': int(input('Введите возраст животного: ')), 
                           'owner_name': input('Введите имя владельца: ')}}
    

def read(): 
    ID = int(input('\nВведите ID животного информацию о котором хотите посмотреть: '))
    if get_pet(ID) != False:
        for  a_name, a_info in get_pet(ID).items():
            print(f'\nЭто {a_info['type']}', end=' ')
            print(f'по кличке "{a_name}".', end=' ')
            print(f'Возраст: {a_info['age']} {get_suffix(a_info['age'])}.', end=' ')  
            print(f'Имя владельца: {a_info['owner_name']}')
    else: 
        print('\nЗапись отсутвует!')

def update():
    ID = int(input('\nВведите ID животного информацию о котором необходимо обновить: '))
    info_up = input('\nЕсли необходимо изменить: \'Имя животного\' введите - 1\nЕсли \'Вид животного\' введите - 2\nЕсли \'Возраст животного\' введите - 3\nЕсли \'Имя владельца\' введите - 4\n\nКакую информацию необходимо обновить?: ')
    if info_up == '1':
        get_pet(ID)[input('Введите новое имя животного: ')] = pets[ID].pop(list(get_pet(ID).keys())[0])
    else:
        for a_info in get_pet(ID).values():
            if info_up == '2':
                a_info['type'] = input('Введите новый вид животного: ')
            elif info_up == '3':
                a_info['age'] = input('Введите новый возраст животного: ')
            elif info_up == '4':
                a_info['owner_name'] = input('Введите новое имя владельца: ')
            else:
                print('Введена неверная команда')

def delete():
    ID = int(input('\nВведите ID животного которого необходимо удалить: '))
    pets.pop(ID)
    print('\nЗапись удалена!')

pets = {
    1:
        {
            "мухтар": {
                "type": "собака",
                "age": 9,
                "owner_name": "павел"
            },
        },
    2:
    {
            "каа": {
                "type": "желторотый питон",
                "age": 19,
                "owner_name": "саша"
            },
        },
    }

command = input('Введите команду: ')

while command !='stop':
    if command == 'создать':
        create()
        command = input('\nВведите команду: ')
    elif command == 'информация':
        read()
        command = input('\nВведите команду: ')
    elif command == 'обновить':
        update()
        command = input('\nВведите команду: ')
    elif command == 'удалить':
        delete()
        command = input('\nВведите команду: ')
    elif command == 'pt':
        pets_list(pets)
        command = input('\nВведите команду: ')
    else:
        print('\nНеверная команда')
        command = input('\nВведите команду: ')
