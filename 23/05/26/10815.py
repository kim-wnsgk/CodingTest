
n = int(input())
nArr = set(list(map(int, input().split())))
m = int(input())
mArr = list(map(int, input().split()))

result = []


for s in mArr:
    if s in nArr:
        result.append(str(1))
    else:
        result.append(str(0))

print(' '.join(result))