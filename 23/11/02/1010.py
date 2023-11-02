import math

a = int(input())
n = [0] * a
m = [0] * a

for i in range(a):
    n[i], m[i] = map(int, input().split())

for i in range(a):
    print(math.comb(m[i], n[i]))