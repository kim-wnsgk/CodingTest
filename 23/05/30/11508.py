n = int(input())
result = 0

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(n):
    if (i+1) % 3 != 0:
        result += arr[i]

print(result)