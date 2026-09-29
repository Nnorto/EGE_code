from math import dist
f = open('27_A_ЕГЭ 2026_День_1.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    x, y, s = [x for x in s.split()]
    color = s[0]
    svet = s[1]
    razmer = s[2:]
    p = [float(x), float(y), color, razmer]
    data.append(p)

print(data[0])
def red_gigant(data):
    red = []
    for x, y, color, razmer in data:
        if color == 'Y' and razmer == 'III':
            red.append([x, y, color, razmer])
    return red
red_gigants = red_gigant(data)

def get_cluster(p0):
    cluster = [p for p in data if dist(p[:2], p0[:2]) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster

clusters = []
print(len(data))
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p[:2], p0[:2]) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print(centers)

dist_red = [dist(centers[1][:2], p[:2]) for p in red_gigants]
print(len(red_gigants))
print(dist_red)
A1 = min(dist_red)
A2 = max(dist_red)
print(int(A1*10_000), int(A2*10_000))

from turtle import *
from random import *
c = 30
tracer(0)
screensize(10_000, 10_000)
up()

for cluster in clusters:
    color = random(), random(), random()
    for x, y, cwet, razmer in cluster:
        goto(x*c, y*c)
        dot(5, color)

for x, y, cwet, razmer in centers:
    goto(x*c, y*c)
    dot(10, 'black')

for x, y, cwet, razmer in red_gigants:
    goto(x*c, y*c)
    dot(10, 'red')

hideturtle()
done()