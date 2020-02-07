#리스트 사칙연산
print('\n리스트 사칙연산')
List1 = [1, 2]
List2 = [3, 4]
print(List1 + List2)

List = [1, 2]
print(List * 3)

#리스트 수정
print('\n리스트 수정')
List = [1, 2, 3, 4]
print(List)
List[1] = 1
print(List)

#리스트 삭제
print('\n리스트 삭제')
List = [1, 2, 3, 4]
print(List)
del List[0]
print(List)

#리스트 삽입
print('\n리스트 삽입')
List = [2, 3]
print(List)
List = [1] + List + [4]
print(List)

#리스트 내장함수
#요소추가(append - 리스트의 마지막에 Value 추가)
print('\n리스트 내장함수(append)')
List = [1, 2, 3, 4]
List.append(5)
print(List)

#요소정렬(sort)
print('\n리스트 내장함수(sort)')
List1 = ['b', 'c', 'a']
List2 = [4, 2, 3, 1]
List1.sort()
List2.sort()
print(List1)
print(List2)

#요소제거(remove - 처음으로 나오는 값 삭제)
print('\n리스트 내장함수(remove)')
List = [2, 1, 2, 3, 4]
List.remove(2)
print(List)

#요소의 개수 세기(count)
print('\n리스트 내장함수(count)')
List = [1, 1, 1, 2, 3]
print(List.count(1))

#리스트 뒤집기(reverse) - sort와 응용해서 내림차순, 올림차순 정렬 사용
print('\n리스트 내장함수(reverse)')
List = [1, 2, 3, 4]
List.reverse()
print(List)

#리스트 확장(extend) - 순서가 있는 집합을 리스트 뒤로 추가
print('\n리스트 내장함수(extend)')
List = [1, 2]
List.extend([3, 4])
print(List)

#리스트 삽입(insert(x, y)) - x자리에 y삽입
print('\n리스트 내장함수(insert)')
List = [1, 2, 3]
List.insert(3, 4)
print(List)

#마지막 요소 꺼내기(pop)
print('\n리스트 내장함수(pop)')
List = [1, 2, 3, 4]
print(List.pop())
print(List)

#요소의 위치 값(index)
print('\n리스트 내장함수(index)')
List = [1, 2, 3, 4]
print(List.index(3))



