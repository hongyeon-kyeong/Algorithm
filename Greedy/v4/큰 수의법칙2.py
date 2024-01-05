n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

rotate_count = m // (k+1)
reside_count = m % (k+1)
result = (first * k + second) * rotate_count + first * reside_count

print(result)

#2

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result = count * first
result += (m-count) * second
