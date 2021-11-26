numb = int(input("Введите целое число: "))
min_divider = numb
max_divider = 1
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        if (min_divider > i):
            min_divider = i
        if (max_divider < i):
            max_divider = i
print("Минимальный равен:", min_divider)
print("Максимальный равен:", max_divider)
