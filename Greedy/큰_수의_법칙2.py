n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k + m % (k+1)
result = count*first

result += (m-count)*second
print(result)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]
count = (m//(k+1))*k + (m%(k+1))

sum += count*first
sum += (m-count) * second

print(sum)