sampleList = [1,1,2,2,3,3,4,4,5,7,7,7,7,7,7]
sampleTuple = (1,2,3,4,5,7,7,7,7,7,7,7,7,7,7)
sampleSet = set(sampleList)
sampleDictionary ={'one':1,'two':2,'three':3}

#시퀀스 자료형의 경우 인덱싱이 가능(list, tuple)
print('List[2]:', sampleList[2])
print('Tuple[2]:', sampleTuple[2])

#인덱싱 불가능
'''
print('Set[2]:', sampleSet[2])
print('Dictionary[2]:', sampleDictionary[2])
'''

#dictionary는 key값을 통해 Value를 찾을 수 있음
print('Dictionary["one"]:',sampleDictionary['one'])
