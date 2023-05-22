n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    i, j, x, y = map(int,input().split())
    sum_ = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
           sum_ += arr[a][b]
    print(sum_)