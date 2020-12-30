'''
stack
- 선입후출, 후입선출
- 별도 라이브러리 없이 리스트로 구현가능
- append() pop()
'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])