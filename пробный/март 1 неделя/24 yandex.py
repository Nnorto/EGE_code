# халява
s = open('24.txt').readline()
s = s.replace('4', 'a')
s = s.replace('3', 'e')
m = 'yandex' * 15  # ну да ручками придется цифры вводить, а потом добавлять +"у" и т.д

print(m in s, len(m), '<= answer')
