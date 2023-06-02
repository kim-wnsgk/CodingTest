n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
result = 0
for i in range(1, n):
    while arr[-i-1] >= arr[-i]:
        arr[-i-1] -= 1
        result += 1
print(result)
