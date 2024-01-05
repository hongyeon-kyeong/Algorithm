n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

result = 0

data.sort()
first = data[-1]
second = data[-2]

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)