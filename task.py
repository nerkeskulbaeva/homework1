count_points = 0

while (True):
    t1 = input('Как зовут преподавтеля - ')
    if (t1  == 'никита соболев' or t1 == 'Никита Соболев' or t1  == 'Никита'):
        count_points += 1
        print('Правильно!')
    else:
        print('Эх, ты')

    t2 = input('Назови функцию для вычисления длины строки - ')
    if ( t2 == 'Len' or t2 == 'len'):
        count_points += 1
        count_len = len(t2)
        print('Правильно, молодец! Длина введенного тобой значения:', count_len)
    else:
        print('Прочитай еще раз первую лекцию')

    t3 = input('Какая функция возвращает максимальное число? - ')
    if (t3 == 'sys.maxsize' or t3 == 'Sys.maxsize'):
        count_points += 1
        print('Правильно!')
    else:
        print('Прочитай еще раз первую лекцию')

    t4 = input('True = ')
    if (t4 == '1'):
        count_points += 1
        print('Правильно, ты молодец!')
    else:
        print('Прочитай еще раз первую лекцию')

    t5 = input('False =')
    if (t5 == '0'):
        count_points += 1
        print('Правильно, 0!')
    else:
        print('Прочитай еще раз первую лекцию')

    t6 = input('Какая функция преобразует переданный ей аргумент в вещественное число? - ')
    if (t6 == 'float'):
        count_points += 1
        print('Правильно, ты молодец!')
    else:
        print('Прочитай еще раз первую лекцию')

    t7 = input('Что лежит в переменной перед тем как мы присвоили ей число? - ')
    if (t7 == 'None' or t7 == 'none' or t7 == '0'):
        count_points += 1
        print('Правильно!')
    else:
        print('Прочитай еще раз первую лекцию')

    t8 = input('Cтандарт кодирования символов? - ')
    if (t8 == 'юникод' or t8 == 'Unicode' or  t8 == 'unicode'):
        count_points += 1
        print('Правильно!')
    else:
        print('Прочитай еще раз первую лекцию')

    t9 = input('Какая функция используется для вывода в Python? - ')
    if (t9 == 'print' or t9 == 'Print'):
        count_points += 1
        print('Правильно')
    else:
        print('Прочитай еще раз первую лекцию')

    t10 = input('Сколько байт занимает кодировка UTF-16 на символ? - ')
    if (t10 == '2'):
        count_points += 1
        print('Правильно!')
    else:
        print('Прочитай еще раз первую лекцию')
		

    replace = input("Хотите повторить тест? - ")
    if (replace == 'да' or replace == 'Да'):
        continue
    elif (replace == 'Нет' or replace == 'нет'):
        print('Количество праивльных ответов: ', count_points)
        print("Спасибо, ты хорошо постарался!")
        break