import math

# 현재 승률과 이긴 게임 횟수 입력
x, y = map(int, input().split())

# 현재 승률 계산
z = (y * 100) // x

# 목표 승률 계산
z_target = z + 1  # 1% 증가

# 목표 승률에 도달하기 위한 최소 게임 횟수 계산
if z >= 99:
    print(-1)  # 현재 승률이 99% 이상이면 목표 승률을 달성할 수 없음
else:
    games_needed = math.ceil(((z_target * x - 100 * y) / (100 - z_target)))
    print(games_needed)