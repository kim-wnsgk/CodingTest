a, b = map(int, input().split())

aa = 1
bb = 1

while a*aa != b*bb:
    if a*aa > b*bb:
        bb += 1
    elif a*aa < b*bb:
        aa += 1

print(a*aa)