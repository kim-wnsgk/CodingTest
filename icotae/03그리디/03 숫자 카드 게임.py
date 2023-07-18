n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

result = 10000

for i in range(n):
    result = min(result, min(arr[i]))

print(result)