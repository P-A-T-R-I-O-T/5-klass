from invalid_menu import invalid_menu_item
from decorator import border_siporaters
import os, shutil, platform, time


num_seconds = 3


def menu_selection(): #Выделение пунктов меню
    print('.'*40, '\n' *2)

def cleaning(): # Очистка терминала
    print('\n' * 40)
@border_siporaters
def new_catalog(): # Функция создание папки
    catalog = int(input('Введите сколько вам папок нужно: '))
    name_catalog = input('Ведите название папки: ')
    for i in range(catalog):
        if not os.path.exists(f"{name_catalog}{i}"):
            if i == 0:
                os.mkdir(f"{name_catalog}")
            elif i > 0:
                os.mkdir(f"{name_catalog}{i}")
            elif i == catalog:
                os.rmdir(f"{name_catalog}{i}")
        else:
            cleaning()
            invalid_menu_item('Такие папки уже существуют')
            break
    
@border_siporaters
def delete_file():
    delet_catalog = input('Ведите название папки: ')
    if os.path.exists(f"{delet_catalog}"):
        os.rmdir(f"{delet_catalog}")
    else:
        cleaning()
        invalid_menu_item('Таких папок нет и не было')
@border_siporaters
def copy():
    name_fail_direct = input('Введите название папки которые нужно скопировать \n')
    if os.path.exists(f"{name_fail_direct}"):
        fail_direct_copy = input('Введите название папки которое будет копией \n')
        shutil.copytree(name_fail_direct, fail_direct_copy)
    else:
        cleaning()
        invalid_menu_item('Такой папки нет!', 3)
@border_siporaters
def view_working_directory():
    print('У вас есть:\n')
    print(os.listdir(),'\n')
    time.sleep(6)
    cleaning()

def attached_directory():
    for something in os.listdir():
        if os.path.isdir(something):
            print(something)
    time.sleep(3)
    cleaning()

def attached_file():

    for something in os.listdir():
        if not os.path.isdir(something):
            print(something)
    time.sleep(3)
    cleaning()
@border_siporaters
def operating_system():
    print('Имя операционной системы: ' ,platform.system() ,platform.release())
    print('Информации об архитектуре:' , platform.architecture())
    print('ведения о базовой платформе:' ,platform.platform())
    print('Реальное имя процессора:',platform.processor())
    print('Тип машины: ' , platform.machine())
    print('Сетевое имя компьютера:' , platform.node())
    time.sleep(11)
@border_siporaters
def creator_program():
    print('Эту программу создал: Колесов Константин 1985 года рождения ')

@border_siporaters
def osnov_menu():
    while True: # Основное меню
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
        print('11. Выход ')
        menu_selection()
        choice = input('Выберите пункт меню: ')
        cleaning()

        if choice == '1':
            cleaning()
            new_catalog()

        elif choice == '2':
            cleaning()
            delete_file()

        elif choice == '3':
            cleaning()
            copy()

        elif choice == '4':
            cleaning()
            view_working_directory()

        elif choice == '5':
            cleaning()
            attached_directory()

        elif choice == '6':
            cleaning()
            attached_file()


        elif choice == '7':
            cleaning()
            operating_system()


        elif choice == '8':
            cleaning()
            creator_program()

        elif choice == '9':
            cleaning()
            from victory import *
            print('\n')
            time.sleep(3)

        elif choice == '10':
            cleaning()
            from use_functions import *  # * обозначает что все модули нужно запускать


        elif choice == '11':
            break


        else:
            invalid_menu_item()

osnov_menu()