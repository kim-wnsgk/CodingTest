s = input()
t = input()

s *= int(50/len(s))
t *= int(50/len(t)) + 1

if s[:50] == t[:50]:
    print(1)
else:
    print(0)
