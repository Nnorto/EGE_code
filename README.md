# Сборник всех заданий, решенных на занятиях
Сюда я буду выкладывать коды со всех наших занятий

# Как решать 18 с роботом?
* Сначала дублирую таблицу, потом пишу =СУММ($A$1:A1), где A1 – начальная клетка
* Растягиваю на первый столбец, первую строчку
* Пишу для B2 во второй таблице – =B2 + МАКС/МИН(клетка сверху; клетка слева)
* растягиваю ~~жопу~~ клетку 
* ??? PROFIT

# 18 робот с полоской
* первую клетку столбца копирую во второй столбец
* во вторую клетку пишу ЕСЛИ(B1>0; ЕСЛИ(ABS(A2−A1)≤10; B1+A2;A2); A2), модуль вам дается в задании
* растягиваем ~~жопу~~ клетку
* выбираем максимум от второго столбца