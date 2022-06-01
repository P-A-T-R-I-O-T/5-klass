def top_menu(): # Верхняя граница меню
    print('*' *40, '\n' *2)

def menu_selection(): #Выделение пунктов меню
    print('.'*40, '\n' *2)

def cleaning(): # Очистка терминала
    print('\n' * 40)

def invalid_menu_item(): # Рамка: Неверного пункт меню
    print('|-|'* 13)
    print('|-|', ' ' * 31, '|-|')
    print('|-|', ' '*5,'Неверный пункт меню', ' '*5, '|-|')
    print('|-|', ' ' * 31, '|-|')
    print('|-|'* 13, '\n'* 2)

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