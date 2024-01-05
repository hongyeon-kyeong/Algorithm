n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())
search = list(map(int, input().split()))
for s in search:
    if array[s] >= 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')