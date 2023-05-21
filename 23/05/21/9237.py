n = int(input())

t = list(map(int, input().split()))

t.sort(reverse=True)

result = 0
for i in range(n):
    result = max(result, (i+2) + t[i])

print(result)