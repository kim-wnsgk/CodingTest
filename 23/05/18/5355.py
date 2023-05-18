n = int(input())

for _ in range(n):
    a, *arr = input().split()
    a = float(a)

    for s in arr:
        if s == '@':
            a *= 3
        elif s == '%':
            a += 5
        elif s == '#':
            a -= 7
        else:
            break

    print(f'{a:.2f}')
