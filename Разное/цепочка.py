N, D, K = map(int, input().split())

x = y = 0
used = {(x, y)}

minX = maxX = x
minY = maxY = y

dx = [1, 0, -1, 0]   # вправо, вверх, влево, вниз
dy = [0, 1, 0, -1]

length = D
direction = 0
done = 0

while done < N:
    # первая сторона длиной length
    step_cnt = min(length, N - done)
    for _ in range(step_cnt):
        x += dx[direction]
        y += dy[direction]
        used.add((x, y))
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
    done += step_cnt
    if done == N:
        break
    direction = (direction + 1) % 4

    # вторая сторона той же длины
    step_cnt = min(length, N - done)
    for _ in range(step_cnt):
        x += dx[direction]
        y += dy[direction]
        used.add((x, y))
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
    done += step_cnt
    if done == N:
        break
    direction = (direction + 1) % 4

    # после двух сторон умножаем D на K
    length *= K

W = maxX - minX + 1
H = maxY - minY + 1
print(H, W)

field = [['.' for _ in range(W)] for _ in range(H)]
for cx, cy in used:
    col = cx - minX
    row = maxY - cy
    field[row][col] = '#'

for row in field:
    print(''.join(row))
