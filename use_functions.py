"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
def no_histori(): #Рамака: Нет истории покупок
    print('|-|'* 13)
    print('|-|', ' ' * 31, '|-|')
    print('|-|', ' '*2, 'У Вас нет истории покупок!', ' '*1, '|-|')
    print('|-|', ' ' * 31, '|-|')
    print('|-|'* 13, '\n'*2)

def no_cash(): # Рамка не хватает средств
    print('|-|'* 13)
    print('|-|', ' ' * 31, '|-|')
    print('|-|', ' '*3, 'У Вас не хватает денег!', ' '*3, '|-|')
    print('|-|', ' '*4, 'Пополните свой баланс', ' '*4, '|-|')
    print('|-|', ' ' * 31, '|-|')
    print('|-|'* 13, '\n'*2)

def no_price(): # Рамка: не корректной цены товара
    print('|-|'* 15)
    print('|-|', ' ' * 37, '|-|')
    print('|-|', ' '*2, 'Не корректная стоимость товара!', ' '*2, '|-|')
    print('|-|', ' ' * 37, '|-|')
    print('|-|'* 15, '\n'*2)

def insufficient_funds (): # Рамка: не хватает средств
    print('|-|'* 13)
    print('|-|', ' ' * 31, '|-|')
    print('|-|', ' '*2, 'У Вас не хватает средств!', ' '*2, '|-|')
    print('|-|', ' '*3, 'Пополните свой баланс!', ' '*4, '|-|')
    print('|-|', ' ' * 31, '|-|')
    print('|-|'* 13, '\n'*2)

def invalid_menu_item(): # Рамка: Неверного пункт меню
    print('|-|'* 13)
    print('|-|', ' ' * 31, '|-|')
    print('|-|', ' '*5, 'Неверный пункт меню', ' '*5, '|-|')
    print('|-|', ' ' * 31, '|-|')
    print('|-|'* 13, '\n'*2)

def cleaning(): # Очистка терминала
    print('\n' * 40)

def menu_selection(): #Выделение пунктов меню
    print('.'*30, '\n' *2)

def top_menu(): # Верхняя граница меню
    print('*' *30, '\n' *2)

def incorrect_amount(): # Рамка: Не корректной суммы пополнения
    print('|-|'* 19)
    print('|-|', ' ' * 49, '|-|')
    print('|-|', ' '*5, 'Не корректная сумма пополнения счёта!', ' '*5, '|-|')
    print('|-|', ' ' * 49, '|-|')
    print('|-|'* 19, '\n' *3)

def replenishment_of_funds(cash): # 1_меню (пополнение счёта)
    top_menu()
    print('Меню пополнение счёта')
    menu_selection()
    amount = input('Пополните счёт: ')
    cleaning()
    while not amount.isdecimal() or not int(amount)>0:
        cleaning()
        incorrect_amount()
        top_menu()
        print('Меню пополнение счёта')
        menu_selection()
        amount = input('Пополните счёт: ')
    cash.append(('Пополнение счёта', int(amount)))
    cleaning()

def purchase(cash): # 2_Меню (Покупка)
    personal_cash = sum([trans[1] for trans in cash])
    if personal_cash == 0:
        insufficient_funds ()
    else:
        top_menu()
        print('Произведите покупку')
        menu_selection()
        amount = input('Введите стоимость товара: ')
        cleaning()
        while not amount.isdecimal() or int(amount)< 1:
            cleaning()
            no_price()
            top_menu()
            print('Произведите покупку')
            menu_selection()
            amount = input('Введите стоимость товара: ')
        if not int(amount) > personal_cash:
            cleaning()
            top_menu()
            print('Произведите покупку')
            menu_selection()
            print('Введите стоимость товара: ', amount)
            name_product = input('Введите наименование продукта: ')
            cleaning()
            cash.append(('Покупка ' + name_product, -int(amount)))
        else:
            cleaning()
            no_cash()

def history(cash):
    cleaning()
    #top_menu()
    #print('Ваша история покупок')
    #menu_selection()
    if len(cash) == 0:
        no_histori()
    else:
        top_menu()
        print('Ваша история покупок')
        menu_selection()
        for name, amount in cash:
            h = (f'> {name} :  {amount}')
            print(filter(q, h))
        #print (h)
            #input('\nНажмите Enter чтобы продолжить ')
            #cleaning()        
def menu():
    cash = [] # Деньги
    while True: # Основное меню
        top_menu()
        personal_cash = sum([trans[1] for trans in cash])
        print('Ваши средства:', personal_cash, '\n')
        print('Главное меню')
        print('1. пополнение счета: ')
        print('2. покупка: ')
        print('3. история покупок: ')
        print('4. выход из программы ')
        menu_selection()
        choice = input('Выберите пункт меню:  ')
        cleaning()

        if choice == '1':
            replenishment_of_funds(cash)
            pass
        elif choice == '2':
            purchase(cash)
            pass
        elif choice == '3':
            history(cash)
            pass
        elif choice == '4':
            break
        else:
            invalid_menu_item()

menu()