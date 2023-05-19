n = int(input())

num = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.insert(num[i], i + 1)

arr.reverse()
print(' '.join(map(str,arr)))