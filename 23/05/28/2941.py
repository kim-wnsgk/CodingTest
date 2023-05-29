n = input()

result = len(n)

for i in range(1, len(n)):
    if (n[i] == '=' and n[i-1] == 'c') or (n[i] == '-' and n[i-1] == 'c') or (n[i] == '-' and n[i-1] == 'd') or (n[i] == 'j' and n[i-1] == 'l') or (n[i] == 'j' and n[i-1] == 'n') or (n[i] == '=' and n[i-1] == 's') or (n[i] == '=' and n[i-1] == 'z'):
        result -= 1
    elif (n[i] == 'z' and n[i-1] == 'd') and (i + 1) < len(n) and n[i+1] == '=':
        result -= 1

print(result)