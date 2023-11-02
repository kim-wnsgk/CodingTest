steps = [(0, -1), (0, -1), (1, 1), (1, 0)]

row, col = map(int, input().split())
point = list(map(int, input().split()))

drt = point.pop()

arr = []

result = 0
for _ in range(row):
    arr.append(list(map(int, input().split())))

while True:
    for i in range(4):
        nextRow = arr[point[0]-1 + steps[(drt+i)%4][0]]
        nextCol = arr[point[1]-1 + steps[(drt+i)%4][1]]
        if 0 < nextRow < row and 0 < nextCol < col:
            if arr[nextRow][nextCol]  == 1:
                point[0] = nextRow, point[1] = nextCol
                result += 1
                continue
