def homework_funktion_filtr ():
    k = input('Какой символ надо найти?') 
    s = input('Создайте список').split() #Создаю СПИСОК, просто ввожу слова через пробел
    a = list(filter(lambda string: k in string.lower(), map(lambda x:x+x, s))) #функция MAP склодывает уже отфильтрованные строки 
    print (a)
homework_funktion_filtr ()
