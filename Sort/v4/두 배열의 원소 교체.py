n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)
result = 0
sum = 0
for i in range(n-k):
    result += array_a[i]
for i in range(k):
    sum += array_b[i]

print(result + sum)

##################
for i in range(k):
    if array_b[i] > array_a[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
        break

print(sum(array_a))
