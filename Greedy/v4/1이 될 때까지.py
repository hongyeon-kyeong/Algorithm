n, k = map(int, input().split())

result = 0

#while True:
#    result += (n % k)
#    n //= k
#    result += 1
#    if n < k:
#        break
#print(result)

#2.
while n > 1:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

print(result)

#3.
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n-1)
print(result)
