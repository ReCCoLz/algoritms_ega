f = open('somefile.txt')
n = int(f.readline())
k = 321
r = [0] * k
ind = [0] * k
sum1 = 0
sumMin = 10 ** 10
iMin = 10**10

for i in range(n):
    x = int(f.readline())
    sum1 = sum1 + x
    ost = sum1 % k
    if r[ost] != 0:
        d = sum1 - r[ost]
        if d < sumMin:
            sumMin = d
            iMin = i - int[ost]
        if d == sumMin:
            iMin = min(iMin, i - ind[ost])
    r[ost] = sum1
    ind[ost] = i
print(iMin)
