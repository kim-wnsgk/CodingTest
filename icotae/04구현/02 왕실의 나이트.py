steps = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)] # 8가지 경우의수

input_point = input()
point = [int(ord(input_point[0]) - ord('a') + 1), int(input_point[1])]
result = 0

for step in steps:
    row = step[0] + point[0]
    col = step[1] + point[1]
    if 0 < row <= 8 and 0 < col <= 8:
        result += 1

print(result)