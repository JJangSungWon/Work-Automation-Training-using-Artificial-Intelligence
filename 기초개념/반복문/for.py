sampleList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 7, 7, 7, 7, 7, 7]
sampleTuple = (1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
sampleSet = {1, 2, 3, 4, 5, 7}
sampleDictionary = {'one': 1, 'two': 2, 'three': 3}

for x in sampleList:
    print('List : ', x)
for x in sampleTuple:
    print('Tuple : ', x)
for x in sampleSet:
    print('Set : ', x)
for x in sampleDictionary:
    print('Dictionary : ', x)

# 배열합 구하기
sumx = 0
for x in [1, 2, 3, 4, 5]:
    sumx += x
print("sumx = ", sumx)

# dictionary를 범위로 지정했을때
회원정보 = {'이름': '홍길동',
        '연락처': '01011112222',
        '주소': '서울시',
        '출생': '930101'}
for a in 회원정보:
    print(a)

# value도 얻고 싶을때
for key, value in 회원정보.items():
    print("{0}:{1}".format(key, value))

# range (시작 값 : 종료 값 : 연속하는 두 수의 차), 종료값은 포함하지 않는다.
for a in range(0, 5, 2):
    print(a)

for a in range(0, 5):
    print(a)

for a in range(5):
    print(a)

listx = [100, 200, 300, 400]
strx = 'abcd'
listxlter = iter(listx)
strxlter = iter(strx)
print(next(listxlter), next(listxlter), next(listxlter), next(listxlter))
print(next(strxlter), next(strxlter), next(strxlter), next(strxlter))

# 다인자 순회
math = [
    ('호준', 100),
    ('지훈', 20),
    ('정민', 70)
]
for i, j in math:
    print(i, j)

# enumerate
for i, j in enumerate([x * 100 for x in range(5)]):
    print(i, j)

