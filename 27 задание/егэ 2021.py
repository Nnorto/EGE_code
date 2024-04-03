f=open("27 пример")
k = int(f.readline())
N=f.readline()

a=list(map(int,f))

maxs  = 0
for i in range(len(a) - k):
    st = sum(a[i: i + k])
    for j in range(i + k, len(a)):
        st += a[j]
        maxs = max(maxs, st)

print(maxs)

