N = 20
f = open("27_A_copy.txt")

a = []
for i in range(N):
    a.append(int(f.readline()))

maxsum = 0
first = 0
second = 0
for i in range(0, N):
    for j in range(i + 1, N):
        if (i<j) and (a[i]>a[j]) and (a[i]+a[j])%120==0 and (a[i]+a[j]) > maxsum:
            maxsum = a[i] + a[j]
            first = a[i]
            second = a[j]
print(first, second)
