n, k = map(int, input().split())

arr = [[0] * 4 for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
    arr[i] = arr[i][1:] + [arr[i][0]]  # 메달 점수 대로 sort 하기 위해 배열 순서 변경

arr.sort(reverse=True)

for i in range(n):
    arr[i].append(i + 1)  # 배열 마지막에 순위 표시
    if i != 0 and arr[i][:3] == arr[i-1][:3]:  # 이전 순위와 동점이면 순위 똑같게
        arr[i][4] = arr[i-1][4]

for i in range(n):
    if arr[i][3] == k:
        print(arr[i][4])
        break
