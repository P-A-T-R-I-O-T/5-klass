from invalid_menu import invalid_menu_item
import os
import time

num_seconds = 5
def top_menu(): # Верхняя граница меню
    print('*' *40, '\n' *2)

def menu_selection(): #Выделение пунктов меню
    print('.'*40, '\n' *2)

def cleaning(): # Очистка терминала
    print('\n' * 40)

def new_catalog(): # Функция создание папки
    new_catalog = input('Введите сколько вам папок нужно: ')
    catalog = int(new_catalog)
    name_catalog = input('Ведите название папки: ')
    for i in range(catalog):
        if not os.path.exists(f"{name_catalog}{i}"):
            os.mkdir(f"{name_catalog}")
        else:
            invalid_menu_item('Такие папки уже существуют')
  
while True: # Основное меню
    top_menu()
    
    print('Главное меню\n')
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
        cleaning
        new_catalog()
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

    elif choice == '12':
        cleaning
        
    else:
        invalid_menu_item()
        time.sleep(num_seconds)
        #Пока конечный вариант. Теперь нужно выполнять задание