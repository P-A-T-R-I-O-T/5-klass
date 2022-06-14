import os


def top_menu(): # Верхняя граница меню
    print('*' *40, '\n' *2)

def menu_selection(): #Выделение пунктов меню
    print('.'*40, '\n' *2)

def cleaning(): # Очистка терминала
    print('\n' * 40)

def invalid_menu_item(error = 'Неверный пункт меню'): # Рамка: Неверного пункт меню
    indent = ' '
    indent_2 = ' '
    if len(error) >= 37: # Работа с длинными предупреждениями
        error_1 = error[:len(error) // 2] # Делим на 2с равные части
        error_2 = error[len(error) //2:]
        
        for char1 in error_2[:5]:  # второую часть, начало строки (до максимального размера страки которая может войти в строку) проверяем на знаки припенания
            if char1 in [' ','.', ',', ':', ';', '!', '?']:
                search1 = error_2.find(char1) # Ищем данный символ в строке
                error_1 = error_1 + error_2[:search1:] #Слияние пер
                error_2 = error_2[search1:] # вычитание не нужных символов
        
    border = '|-|' 
    print(border * 13)    # Печатаем верхнюю рамки
    len(border +indent * 33 + border)
    
    if len(error) >= 37: # В случаи когда главный параметр больше максимального значения, выравниваем по центру рамки
        if len(border + indent + error_1 + indent_2 + border) < 39:
            while len(border + indent + error_1 + indent_2 + border) <= 38:
                indent += ' '
                indent_2 += ' '
            if len(border + indent + error_1 + indent_2 + border) > 39:
                indent = indent[1:]
            print(border + indent + error_1 + indent_2 + border)
            indent = ' '
            indent_2 = ' '
        #else:
        #    print(border, indent, error_1, indent_2, border)
        if len(border + indent + error_2 + indent_2 + border) < 39:
            while len(border + indent + error_2 + indent_2 + border) <= 38:
                indent += ' '
                indent_2 += ' '
            if len(border + indent + error_2 + indent_2 + border) > 39:
                indent = indent[1:]
            print(border + indent + error_2 + indent_2 + border)
    
    elif len(error) < 37:  # В случаи когда главный параметр маленькое значение, выравниваем по центру рамки
        indent = ' '
        indent_2 = ' '
        while len(border + indent + error + indent_2 + border) <= 38:
            indent += ' '
            indent_2 += ' '
        if len(border + indent + error + indent_2 + border) > 39:
                indent = indent[1:]
        print(border + indent + error + indent_2 + border)
    indent = ' '
    print(border + indent * 33 + border)
    print(border * 13)
    #print('|-|', indent * 31, '|-|')
    print('\n'* 2)
    print('|-|'* 13, '\n'* 2)

def new_catalog(): # Функция создание папки
    new_catalog = input('Введите сколько вам папок нужно: ')
    catalog = int(new_catalog)
    name_catalog = input('Ведите название папки: ')
    for i in range(catalog):
        if not os.path.exists(f"{name_catalog} {i}"):
            if i == 0:
                os.mkdir(f"{name_catalog}")
            else:
                os.mkdir(f"{name_catalog} {i}")

while True: # Основное меню
    top_menu()
    
    print('Главное меню')
    print('1. создать папку: ')
    print('2. удалить (файл/папку): ')
    print('3. копировать (файл/папку): ')
    print('4. просмотр содержимого рабочей директории: ')
    print('5. посмотреть только папки: ')
    print('6. посмотреть только файлы: ')
    print('7. просмотр информации об операционной системе: ')
    print('8. создатель программы: ')
    print('9. играть в викторину: ')
    print('10. мой банковский счет: ')
    print('11. смена рабочей директории: ')
    print('Выход: ')
    menu_selection()
    choice = input('Выберите пункт меню: ')
    cleaning()

    if choice == '1':
        new_catalog()
        cleaning
    elif choice == '2':
        
        cleaning
    elif choice == '3':
        
        cleaning
    elif choice == '4':
        
        cleaning
    elif choice == '5':
        
        cleaning
    elif choice == '6':
        
        cleaning
    elif choice == '7':
        
        cleaning
    elif choice == '8':
        
        cleaning
    elif choice == '9':
        
        cleaning
    elif choice == '10':
        
        cleaning
    elif choice == '11':
        cleaning
    else:
        invalid_menu_item()
        print(len('|-|'* 13))
        #Покуа конечный вариант. Теперь нужно выполнять задание