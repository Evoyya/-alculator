def culc(string):
    string = string.strip() # убираю лишние пробелы вначале и в конце 
    list_line = string.split(' ')
    # list_line — список с элементами входящей строки

    book = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5', 'шесть': '6',
            'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10', 'одиннадцать': '11',
            'двенадцать': '12', 'тринадцать': '13', 'четырнадцать': '14', 'пятнадцать': '15', 'шестнадцать': '16',
            'семнадцать': '17', 'восемнадцать': '18', 'девятнадцать': '19', 'двадцать': '20',
            'тридцать': '30', 'сорок': '40', 'пятьдесят': '50', 'шестьдесят': '60', 'семьдесят': '70',
            'восемьдесят': '80', 'девяносто': '90', 'минус': '-', 'плюс': '+', 'умножить': '*', 'на': '',
            'открывается': '(', 'закрывается': ')', 'скобка': '', 'сто': '100', 'двести': '200', 'триста': '300',
            'четыреста': '400', 'пятьсот': '500', 'шестьсот': '600', 'семьсот': '700', 'восемьсот': '800',
            'девятьсот': '900', 'одна тысяча': '1000', 'две тысячи': '2000', 'три тысячи': '3000',
            'четыре тысячи': '4000', 'пять тысяч': '5000', 'шесть тысяч': '6000', 'семь тысяч': '7000',
            'восемь тысяч': '8000', 'девять тысяч': '9000', 'ноль': '0'}
    # словарь с минимальным наборо пар ключ+значение для перевода строки в число

    # посимвольный перевод строки в число (используя словарь и список)
    result = ''
    if string == '':
        return 'Неверный ввод'
    for ind in range(0,len(list_line)):
        if list_line[ind] in book:
            if book[list_line[ind]].isnumeric():
                if ind > 0 and book[list_line[ind-1]].isnumeric():
                    pass
                elif ind != len(list_line) - 1:
                    if list_line[ind+1] in book:
                        if book[list_line[ind+1]].isnumeric():
                            result += str(int(book[list_line[ind]]) + int(book[list_line[ind+1]]))
                        else:
                            result += book[list_line[ind]] # Если следующий элемент не число
                    else:
                        return 'Неверный ввод' # если следующий элемента нет в словаре, то неверный ввод
                else:
                    result += book[list_line[ind]] #одиночное число
            else:
                result += book[list_line[ind]] # если это не число, а знак
        else:
            return 'Неверный ввод' # если нет в словаре, то неверный ввод

    # Проверяем что количество скобок правильное
    if result.count('(') != result.count(')'):
        return 'Неверный ввод'

    # Получаем результат выражения с помощью eval()
    int_result = eval(result)
    str_result = str(int_result)


    total = '' #итоговый результат

    # Записываем минус
    if int_result < 0:
        total += 'минус'
        str_result = str_result[1:]
        int_result = str(str_result)

    # Меняю в словаре местами ключ и значение
    invbook = {v: k for k, v in book.items()}

    # Проверяю уникальные числа
    if 11<= int_result <= 19 or int_result == 0:
        total += invbook[str_result]
    # Перевожу остальные числа
    else:
        delit = '1' + '0' * len(str_result) # делитель чтобы разделять числа >= 100
        for el in range(len(str_result)):
            if int(str(int_result % int(delit) - int_result % int(delit[:-1]))) != 0 and not(11 <= int(str(int_result % int(delit))) <= 19):# не берём уникальные числа, взяли уже раньше 
                total += invbook[str(int_result % int(delit) - int_result % int(delit[:-1]))] + ' ' # 987 => 900-80-7 
            elif 11 <= int(str(int_result % int(delit))) <= 19:
                total += invbook[str(int_result % int(delit))]
                break
            delit = delit[:-1]
    # Возвращаю результат работы программы
    return total



# !!! Начало работы !!!

string = input('Введите математическое выражение написанное буквами: ')
print(culc(string))

