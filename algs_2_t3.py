"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""


def reversal_num(num):
    if len(str(num)) == 1:
        return num
    else:
        return int(str(num % 10) + str(reversal_num(num // 10)))


num = int(input('Введите натуральное число\n'))
r = reversal_num(num)
print(r)
