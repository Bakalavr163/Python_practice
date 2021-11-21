# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 0,62 мили
def convert(km):
    miles = km / 1.609
    return miles

kilo_meter = float(input("Введите единицу в километрах:\n"))
# вызываем функцию
miles = convert(kilo_meter)
print("Значение еденицы в милях:\n", miles)

# Результат
# Введите единицу в километрах:
# 5
# Значение еденицы в милях:
# 3.106855



# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

def my_round(number, ndigits):
    number = str(number)
    strk = '0.'  
    index = number.find('.')
    ch = number[index + ndigits + 1]  
    number = number[:(index + ndigits + 1)]  
    if ch in ['5', '6', '7', '8', '9']:
        strk = (strk + '0' * (ndigits - 1) + '1')
        if float(number) >= 0:
            anser = float(number) + float(strk)
        else:
            anser = -(abs(float(number)) + float(strk))
    else:
        anser = float(number)
    return anser
print(my_round(2.1234467, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Результат 
# 2.12345
# 2.2
# 3.0


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


def lucky_ticket(ticket_number):
    ticket = str(ticket_number)
    ch1 = 0
    ch2 = 0
    if (len(ticket) % 2) == 0:
        for i, element in enumerate(ticket):
            if i <= (int((len(ticket) - 1) / 2)):
                ch1 = ch1 + float(element)
            elif (int((len(ticket) - 1) / 2)) < i < int(len(ticket)):
                ch2 = ch2 + float(element)
            else:
                anser = "Допущена ошибка"
                return anser
    else:
        anser = "Билет {} неправильный билет".format(ticket_number)
        return anser
    if ch1 == ch2:
        anser = "Билет {} счастливый".format(ticket_number)
        return anser
    else:
        anser = "Билет {} несчастливый".format(ticket_number)
        return anser
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Результат
# Билет 123006 счастливый
# Билет 12321 неправильный билет
# Билет 436751 счастливый