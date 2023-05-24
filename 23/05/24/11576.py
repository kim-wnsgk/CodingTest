a, b = map(int, input().split())

m = int(input())

num = [0] * m
num = list(map(int, input().split()))

value = 0
result = []

num.reverse()
for i in range(m):
    value += num[i] * pow(a, i)

while value:
    result.append(str(value % b))
    value //= b

result.reverse()
print(" ".join(result))
