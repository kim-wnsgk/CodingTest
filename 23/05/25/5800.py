n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))

    newArr = arr[1:]
    newArr.sort(reverse=True)
    largestGap = 0


    for j in range(arr[0] - 1):
        largestGap = max(largestGap, newArr[j] - newArr[j+1])

    print('Class', i+1)
    print(f'Max {max(arr[1:])}, Min {min(arr[1:])}, Largest gap {largestGap}')
