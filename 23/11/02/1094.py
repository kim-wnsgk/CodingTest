n = int(input())

count = 0

_sum = 0
log = 64

while _sum != n:  # 길이 더한 값이 입력값과 같을때까지 반복
    if _sum + log <= n:  # 길이 더한 값이 입력값보다 작다면 더함
        _sum += log
        count += 1
    else:  # 크다면 나뭇가지를 반으로 나눔
        log /= 2

print(count)