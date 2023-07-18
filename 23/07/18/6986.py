n, k = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(float(input()))
arr.sort()

arr_a = arr[k:-k]

arr_b = []
arr_b += [arr_a[0]] * k
arr_b += arr_a
arr_b += [arr_a[-1]] * k

print(round(sum(arr_a) / len(arr_a), 2))
print(round(sum(arr_b) / len(arr_b), 2))
