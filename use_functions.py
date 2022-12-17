"""
В файл нужно записать переменные:
    personal_cash (сколько денег на считу)
    amount  (не посредственно деньги)
    name назхвание товара
"""
import pickle, os
from invalid_menu import invalid_menu_item, cleaning

BALANSE = 'balanse.data'
FILE_NAME = 'purchase_history.data'

if os.path.exists(BALANSE):
    with open(BALANSE, 'rb') as f:
        balanse = pickle.load(f)

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        cash = pickle.load(f)

def menu_selection(): #Выделение пунктов меню
    print('.'*30, '\n' *2)

def top_menu(): # Верхняя граница меню
    print('*' *30, '\n' *2)


def replenishment_of_funds(cash): # 1_меню (пополнение счёта)
    top_menu()
    print('Меню пополнение счёта')
    menu_selection()
    amount = input('Пополните счёт: ')
    cleaning()
    while not amount.isdecimal() or not int(amount)>0:
        cleaning()
        invalid_menu_item('Не корректная сумма пополнения счёта!')
        top_menu()
        print('Меню пополнение счёта')
        menu_selection()
        amount = input('Пополните счёт: ')
    cash.append(('Пополнение счёта', int(amount)))
    cleaning()

def purchase(cash): # 2_Меню (Покупка)
    personal_cash = sum([trans[1] for trans in cash])
    if personal_cash == 0:
        invalid_menu_item('У Вас не хватает средств! Пополните свой баланс!')
    else:
        top_menu()
        print('Произведите покупку')
        menu_selection()
        amount = input('Введите стоимость товара: ')
        cleaning()
        while not amount.isdecimal() or int(amount)< 1:
            cleaning()
            invalid_menu_item('Не корректная стоимость товара!')
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
            invalid_menu_item('У Вас не хватает денег! Пополните свой баланс')

def history(cash):
    cleaning()
    if len(cash) == 0:
        invalid_menu_item('У Вас нет истории покупок!')
    else:
        top_menu()
        print('Ваша история покупок')
        menu_selection()
        for name, amount in cash:
            print(f'> {name} :  {amount}')
            input('\nНажмите Enter чтобы продолжить ')
            cleaning()        
def menu():
    cash = [] # Деньги
    while True: # Основное меню
        top_menu()
        if os.path.exists(BALANSE):
            if balanse == 0:
                personal_cash = sum([trans[1] for trans in cash])
                print('Ваши средства:', personal_cash, '\n')
            else:
                print('Ваши средства:', balanse, '\n')
        else:
            personal_cash = sum([trans[1] for trans in cash])
            print('Ваши средства:', personal_cash, '\n')
        print('Главное меню')
        print('1. пополнение счета: ')
        print('2. покупка: ')
        print('3. история покупок: ')
        print('4. сохранить историю')
        print('5. выход из программы ')
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
            with open(FILE_NAME, 'wb') as f:
                pickle.dump(cash, f)
        elif choice == '5':
            with open(BALANSE, 'wb') as f:
                pickle.dump(personal_cash, f)
            break
        else:
            invalid_menu_item('Неверный пункт меню')

menu()