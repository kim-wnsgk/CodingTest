n, game = input().split()
n = int(n)

maxPeople = 0
if game == 'Y':
    maxPeople = 1
elif game == 'F':
    maxPeople = 2
elif game == 'O':
    maxPeople = 3

arr = []
for _ in range(n):
    arr.append(input())
arr = list(set(arr))

print(len(arr) // maxPeople)
