a, b, c = map(int, input().split())
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# 특정 수에 대한 두 수의 합 또는 곱의 나머지는 특정 수에 대한 두 수의 나머지의 합 또는 곱의 나머지와 동일하다.
