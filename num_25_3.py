numb = int(input("Введите целое число: "))
sum_of_dividers = 0
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        sum_of_dividers += i
print("Сумма:", sum_of_dividers)
