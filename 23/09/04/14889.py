from itertools import combinations


def calculate_team_ability(team, skills):
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += skills[team[i]][team[j]] + skills[team[j]][team[i]]
    return ability


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모든 조합을 생성
all_players = set(range(n))
min_ability_diff = float('inf')

for team_a in combinations(all_players, n // 2):
    team_b = tuple(all_players - set(team_a))

    ability_a = calculate_team_ability(team_a, s)
    ability_b = calculate_team_ability(team_b, s)

    ability_diff = abs(ability_a - ability_b)

    if ability_diff < min_ability_diff:
        min_ability_diff = ability_diff

print(min_ability_diff)
