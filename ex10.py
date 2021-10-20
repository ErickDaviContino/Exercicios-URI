s = 0
t = int(input())


for i in range(t):
    n, k = map(int, input().split())

    if n >= k:
        s = s + n/k
        s = s + n % k
    else:
        s = n
    print(int(s))
    s = 0
    t -= 1
