x = int(input())
#그냥 최대값으로 테이블 선언
d = [0] * 30001
#d = [0] * x

for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    #현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    #현재의 수가 5로 나누어 떨어지는 경우
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])
#for i in range(x):, d[1]은 0이니까 계산하지 않고, x까지 계산하기 위해서 x+1로 선언
    #init_num = i
    #result = 0
    #while d[i] == 0:
    #    if i == 0:
    #        break
    #    if i % 5 == 0:
    #        i //= 5
    #    elif i % 3 == 0:
    #        i //= 3
    #    elif i % 2 == 0:
    #        i //= 2
    #    else:
    #        i -= 1
    #    result += 1
    #d[init_num] = d[i] + result
#print(d[x-1])



