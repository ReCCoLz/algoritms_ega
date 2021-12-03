numb = int(input("Введите целое число: "))
count_of_dividers = 0
for i in range(numb - 1, 1, -1):
    if numb % i == 0:
        count_of_dividers += 1
print("Количество равно:", count_of_dividers)
