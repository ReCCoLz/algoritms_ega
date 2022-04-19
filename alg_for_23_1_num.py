N = 776
f = open("27_A_copy.txt")

a = []
for i in range(N):
    a.append(int(f.readline()))

maxsum = 0
maxlen = 0
cursum = 0
curlen = 0
for i in range(0, N):
    cursum = a[i]
    curlen = 1
    for j in range(i + 1, N):
        cursum += a[j]
        curlen += 1
        if cursum >= maxsum and cursum % 43 == 0:
            maxlen = curlen
            maxsum = cursum
            print(maxsum, maxlen)
