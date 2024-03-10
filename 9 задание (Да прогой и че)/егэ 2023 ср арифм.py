f = open('файлы/KIM_0015973096_9')
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    count_num = [] # количество чисел
    sr_z = sum(a)/len(a)
    for x in a:
        count_num.append(a.count(x))
    if count_num.count(2) == 4 and count_num.count(1) == 3:
        rep_num = [x for x in a if a.count(x) > 1]
        sr_rep = sum(rep_num)/len(rep_num)
        if sr_rep > sr_z:
            count += 1

print(count)