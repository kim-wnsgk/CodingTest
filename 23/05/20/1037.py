count = int(input())
divisors = list(map(int, input().split()))

divisors.sort()

N = divisors[0] * divisors[-1]

print(N)