"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

num = int(input("Введите натуральное число (условно х). Для завершения введите 0.\n x = "))
max_num = 0
max_sum = 0
while num != 0:
    new_num = num
    my_sum = 0
    while num > 0:
        my_sum += num % 10
        num //= 10
    if my_sum > max_sum:
        max_sum = my_sum
        max_num = new_num
    num = int(input("Введите натуральное число.\n x = "))

print(f'\nВывод:\nЧисло {max_num} имеет максимальную сумму цифр равную {max_sum}')
