n, k = map(int, input().split())
coin = []
for _ in range(n) :
	coin.append(int(input()))

coin.sort(reverse=True)

sum = 0
for c in coin :
	if c > k :
		continue
	sum += k//c
	k %= c

print(sum)