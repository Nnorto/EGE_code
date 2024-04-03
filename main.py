n = int(input())
p2 = n//100 # 36
pp2 = n % 100 # 63
s1 = p2 //10 + p2%10 # 3 + 6
s2  = pp2 //10 + pp2%10 # 6 + 3
print(s1//s2)

