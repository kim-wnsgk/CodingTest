n = int(input())

arr = input().split()

place = [1,1]

for i in range(len(arr)):
    if arr[i] == 'L':
        if place[1] > 1:
            place[1] -= 1
    elif arr[i] == 'R':
        if place[1] < n:
            place[1] += 1
    elif arr[i] == 'U':
        if place[0] > 1:
            place[0] -= 1
    elif arr[i] == 'D':
        if place[0] < n:
            place[0] += 1

print(' '.join(map(str, place)))