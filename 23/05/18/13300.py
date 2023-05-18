import math

n, k = map(int, input().split())

students = [[0]*2 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        students[y-1][0] += 1
    else:
        students[y-1][1] += 1

room = 0

for i in range(len(students)):
    for j in range(len(students[i])):
        if students[i][j] == 0:  # 메모리 절약
            continue
        room += math.ceil(students[i][j] / k)

print(room)