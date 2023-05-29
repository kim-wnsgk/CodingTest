n, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

n = str(n)

result = '0' * len(n)
for i in range(len(n)):
    for j in range(k):
        new_result = int(result[:i] + str(arr[j]) + result[i+1:])
        if new_result <= int(n):
            result = str(new_result)

print(int(result))