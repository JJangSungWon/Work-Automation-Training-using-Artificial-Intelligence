sampleList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 7, 7, 7, 7, 7, 7]
sampleTuple = (1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
sampleSet = {1, 2, 3, 4, 5, 7}
sampleDictionary = {'one': 1, 'two': 2, 'three': 3}

# \는 개행문자입니다.
print("List: ", sampleList, \
      ', type:', type(sampleList))

print("Tuple: ", sampleTuple, \
      ', type:', type(sampleTuple))

print("Set: ", sampleSet, \
      ', type:', type(sampleSet))

print("Dictionary: ", sampleDictionary, \
      ', type:', type(sampleDictionary))

# List(동일한 리스트 안에 다른 자료형 저장 가능)
List1 = [1, 2, 3]
List2 = ['a', 'b', 'c']
List3 = ['수학', 95, 'A+']

# Tuple(리스트와 달리 원소 변경이 불가능하다) - dictionary의 key값으로 쓸 때 유용
Tuple1 = (1, 2, 3)
Tuple2 = ('a', 'b', 'c')
Tuple3 = ('수학', 95, 'A+')
