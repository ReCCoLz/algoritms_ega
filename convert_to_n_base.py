n = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
k = 16

ls = []

while n > 0:
    n, a = divmod(n, k)
    ls = [a] + ls
print(ls.count(0))