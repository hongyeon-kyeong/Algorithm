# sorted() : 정렬된 새로운 배열을 리턴
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

# sort() : 입력 배열을 정렬
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

# key를 활용한 정렬
array = [('바나나', 2), ('사과',5), ('당근', 3)]

def setting(data) :
	return data[1]

result = sorted(array, key=setting)
print(result)

# key를 활용한 정렬 - lambda
array = [('바나나', 2), ('사과',5), ('당근', 3)]
result = sorted(array, key = lambda x : x[1])

print(result)

'''
lambda 인자 : 표현식
-> 인자를 받아서 표현식을 거쳐 반환한다.
'''

print((lambda a,b : a+b)(3,7))