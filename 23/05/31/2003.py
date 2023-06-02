n, m = map(int, input().split())

arr = list(map(int,input().split()))
result = 0

for i in range(n):
    sum_ = 0
    for j in range(i, n):
        if sum_ < m:
            sum_ += arr[j]
        if sum_ == m:
            result += 1
            break
        elif sum_ > m:
            break

print(result)