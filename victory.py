from invalid_menu import invalid_menu_item
from decorator import border_siporaters
import random
numbers = [
    ('Александр Сергеевич Пушкин', '6.6.1799'),
    ('Михаил Васильевич Ломоносов', '19.11.1711'),
    ('Михаил Илларионович Кутузов', '16.9.1745'),
    ('Иосиф Виссарионович Джугашвили', '21.12.1878'),
    ('Владимир Владимирович Путин', '7.10.1952'),
    ('Константин Эдуардович Циолковский', '17.9.1857'),
    ('Иван Васильевич Рюрикович', '25.8.1530'),
    ('Георгий Константинович Жуков', '1.12.1896'),
    ('Дмитрий Иванович Менделеев', '8.2.1834'),
    ('Айзек Азимов', '4.10.1919')
]
#Дата прописью
@border_siporaters
def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' +
        month_list[int(date_list[1]) - 1] + ' ' +
        date_list[2] + ' года')
# количество случайных элементов
result = random.sample(numbers, 5)
# Сама викторина
victory_play = 'да'
while victory_play.lower() == 'да':
    mistakes_count = 0
    for name, birthdate in result:
        answer = input(f'Какая дата рождения у {name}?' '\n')
        if answer != birthdate:
            date = birthdate
            print(get_date(date))
            mistakes_count += 1
    right_answers_count = len(result)-mistakes_count
    print(f'Итак, у вас {right_answers_count} правильных ответов и {mistakes_count} неправильных ответов')
    if right_answers_count == 5:
        invalid_menu_item('Поздравляем Вы ПОБЕДИТЕЛЬ!!!')
        break
    elif right_answers_count > 0:
        invalid_menu_item('Хороший результат, Вы молодец.')
        break
    elif right_answers_count == 0:
        invalid_menu_item('К сожелению Вы проиграли.')
        break
