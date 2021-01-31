n = int(input())
coins = [500,100,50,10,5,1]
count = 0
k = 1000-n

for coin in coins :
	if k < coin :
		continue
	count += (k//coin)
	k %= coin

print(count)	