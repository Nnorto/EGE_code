f = open('файлы/9_9832-2')
sums = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    count_num = [] # количество чисел
    for x in a:
        count_num.append(a.count(x))

    if count_num.count(2) == 4 and (count_num[-1] != 2):
        sums += sum(a)
        break
print(sums)