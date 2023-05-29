n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))
k.sort(reverse=True)

weight = 0
for i in range(n):
    weight = max(weight, k[i] * (i+1))

print(weight)