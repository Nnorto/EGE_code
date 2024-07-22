
for n in reversed(range(4, 10000)):  # да да на этом ловят привыкай
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    summa = s.count('1') + s.count('2') * 2 + s.count('5') * 5

    # есть еще способ как найти сумму, через функцию map()

    summa = sum(list(map(int, s)))
    if summa == 64:
        print(n)


from ipaddress import *
for A in range(16, 25):
    net = ip_network(f'117.157.2.8/{A}', 0)
    flag = True
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') < ad_bin[16:].count('1'):
            flag = False
            break
    if flag:
        print(A)

print('или')

for A in range(9):
    net = ip_network(f'117.157.2.8/{16+A}', 0)
    flag = True
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') < ad_bin[16:].count('1'):
            flag = False
            break
    if flag:
        print(A)
