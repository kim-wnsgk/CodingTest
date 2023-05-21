n = int(input())

strs = [''] * n

for i in range(n):
    strs[i] = str(input())

result = ''

for i in range(len(strs[0])):
    diff = False  # 하나라도 다른 문자가 있다면 True로
    c = strs[0][i]  # 첫번째 문자열의 문자를 기준으로 비교
    for s in strs:
        if s[i] != c: diff = True
    if diff:
        result += '?'
    else:
        result += c

print(result)