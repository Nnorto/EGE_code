alf = 'екмопртью'
count = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1+x2+x3+x4+x5
                    count += 1
                    if s[0] != 'е' and s.count('к') == 2:
                        print(count)
                        exit()
