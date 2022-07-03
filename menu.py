from invalid_menu import invalid_menu_item
import os, shutil
import os
import time


num_seconds = 3
def top_menu(): # Верхняя граница меню
    print('*' *40, '\n' *2)

def menu_selection(): #Выделение пунктов меню
    print('.'*40, '\n' *2)

def cleaning(): # Очистка терминала
    print('\n' * 40)

def new_catalog(): # Функция создание папки
    catalog = int(input('Введите сколько вам папок нужно: '))
    name_catalog = input('Ведите название папки: ')
    for i in range(catalog):
        if not os.path.exists(f"{name_catalog}{i}"):
            os.mkdir(f"{name_catalog}{i}")
        else:
            cleaning()
            invalid_menu_item('Такие папки уже существуют')
            break
    

def delete_file():
    # Если количество папок введёного больше, чем существует, он всё ровно удалит и напишен сообщение
    invalid_menu_item('Задайте ровно то количество пакок которое нужно удалить', 5)
    invalid_menu_item('повторного удаление не будет!')
    catalog = int(input('Введите сколько папок нужно удалить: '))
    delet_catalog = input('Ведите название папки: ')
    for i in range(catalog):
        if os.path.exists(f"{delet_catalog}{i}"):
            os.rmdir(f"{delet_catalog}{i}")
        else:
            cleaning()
            invalid_menu_item('Таких папок нет и не было')
            break

def copy():
    print('Вы находитесь здесь:')
    print(os.getcwd())
    print('У вас есть:\n')
    print(os.listdir(),'\n')
    name_fail_direct = input('Введите название файла/папки которые нужно скопировать \n')
    fail_direct_copy = name_fail_direct + '_копия'
    shutil.copy(name_fail_direct, fail_direct_copy)

def view_working_directory():
    print('У вас есть:\n')
    print(os.listdir(),'\n')
    time.sleep(6)
    cleaning

def attached_directory():
    for something in os.listdir():
        if os.path.isdir(something):
            print(something)
    time.sleep(6)
    cleaning

def attached_file():
    for something in os.listdir():
        if not os.path.isdir(something):
            print(something)
    time.sleep(6)
    cleaning
    
while True: # Основное меню
    top_menu()
    
    print('Главное меню\n')
    print('1. создать папку: ')
    print('2. удалить (файл/папку): ')
    print('3. копировать файл: ')
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
        delete_file()

    elif choice == '3':    
        cleaning
        copy()

    elif choice == '4':   
        cleaning
        view_working_directory()

    elif choice == '5':        
        cleaning
        attached_file()

    elif choice == '6':        
        cleaning
        attached_directory()

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