n, m = map(int, input().split())

arr = []

for i in range(n):
    newArr = [i+1]
    for j in range(n):
        if len(newArr) >= m:
            continue
        if (j+1) in newArr:
            continue
        newArr.append(j+1)
    arr.append(newArr)

print(arr)