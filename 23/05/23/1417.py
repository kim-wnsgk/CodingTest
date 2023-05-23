n = int(input())

people = [0] * n
for i in range(n):
    people[i] = int(input())
count = 0

while(1):
    for i in range(1, n):
        if people[i] == max(people):
            people[0] += 1
            people[i] -= 1
            count += 1
    if people[0] == max(people):
        for i in range(1, n):
            if people[0] == people[i]:
                people[0] += 1
                people[i] -= 1
                count += 1
        break

print(count)