import math

t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))
result = []

for n in arr:
    same = '0'  # 회문인 수가 존재할 때
    for i in range(2, 65):  # 2부터 64까지 진법 변환
        n2 = n
        num = []

        while n2 != 0:  # 진법 변환하여 배열 생성
            num.append(n2 % i)
            n2 //= i

        isSame = '1'

        for j in range(math.ceil(len(num) / 2)):  # 0, -1 / 1, -2 순서로 비교
            if num[j] != num[-j-1]:  # 하나라도 다른값 있다면 존재하지 않음
                isSame = '0'
                break
        same = isSame

        if same == '1':
            break

    result.append(same)

print(' '.join(result))