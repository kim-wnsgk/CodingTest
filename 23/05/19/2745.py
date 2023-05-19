import math

n, b = input().split()
b = int(b)

result = 0

for i in range(len(n)):
    inv = -i-1
    if n[inv] == 'A': result += 10 * math.pow(b, i)
    elif n[inv] == 'B': result += 11 * math.pow(b, i)
    elif n[inv] == 'C': result += 12 * math.pow(b, i)
    elif n[inv] == 'D': result += 13 * math.pow(b, i)
    elif n[inv] == 'E': result += 14 * math.pow(b, i)
    elif n[inv] == 'F': result += 15 * math.pow(b, i)
    elif n[inv] == 'G': result += 16 * math.pow(b, i)
    elif n[inv] == 'H': result += 17 * math.pow(b, i)
    elif n[inv] == 'I': result += 18 * math.pow(b, i)
    elif n[inv] == 'J': result += 19 * math.pow(b, i)
    elif n[inv] == 'K': result += 20 * math.pow(b, i)
    elif n[inv] == 'L': result += 21 * math.pow(b, i)
    elif n[inv] == 'M': result += 22 * math.pow(b, i)
    elif n[inv] == 'N': result += 23 * math.pow(b, i)
    elif n[inv] == 'O': result += 24 * math.pow(b, i)
    elif n[inv] == 'P': result += 25 * math.pow(b, i)
    elif n[inv] == 'Q': result += 26 * math.pow(b, i)
    elif n[inv] == 'R': result += 27 * math.pow(b, i)
    elif n[inv] == 'S': result += 28 * math.pow(b, i)
    elif n[inv] == 'T': result += 29 * math.pow(b, i)
    elif n[inv] == 'U': result += 30 * math.pow(b, i)
    elif n[inv] == 'V': result += 31 * math.pow(b, i)
    elif n[inv] == 'W': result += 32 * math.pow(b, i)
    elif n[inv] == 'X': result += 33 * math.pow(b, i)
    elif n[inv] == 'Y': result += 34 * math.pow(b, i)
    elif n[inv] == 'Z': result += 35 * math.pow(b, i)
    else: result += int(n[inv]) * math.pow(b, i)

print(int(result))