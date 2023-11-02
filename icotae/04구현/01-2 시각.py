n = int(input())

result = 0

for i in range(n+1):
    for j in range(60):
        for h in range(60):
            tm = str(i)+str(j)+str(h)
            if '3' in tm:
                result += 1

print(result)