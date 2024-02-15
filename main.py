def jopa(aray, flag):
    ch_count = 0
    nch_count = 0
    n = aray
    for i in range(len(n)):
        if n[i] % 2 == 0:
            ch_count += 1
        else:
            nch_count += 1

    if flag:
        return ch_count
    else:
        return nch_count

# создает массив чисел из последовательности
def posled():
    s = input()
    a = s.split()  # это теперь массив
    for x in range(len(a)):
        a[x] = int(a[x])
    return a

mas = posled()
mas2 = posled()
print(jopa(mas, True), jopa(mas2, False))
