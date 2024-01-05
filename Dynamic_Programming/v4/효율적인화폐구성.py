n, m = map(int, input().split())
coins = [0] * n
d = [10001] * (m+1)
for i in range(n):
    coins[i] = int(input())

d[0] = 0
for i in range(n):
#    result = 1000000
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != 10001:
            d[j] = min(d[j], d[j-coins[i]] + 1)
#        if i - coin == 0:
#            d[i] = 1
#        if i - coin > 0:
#            if d[i-coin] == -1:
#                continue
#           d[i] = min(result, d[i-coin]) + 1

if d[m] == 10001:
    print(-1)
else:
    print(d[m])