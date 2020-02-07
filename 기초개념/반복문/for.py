sampleList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 7, 7, 7, 7, 7, 7]
sampleTuple = (1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
sampleSet = {1, 2, 3, 4, 5, 7}
sampleDictionary = {'one':1, 'two':2, 'three':3}

for x in sampleList:
    print('List : ', x)
for x in sampleTuple:
    print('Tuple : ', x)
for x in sampleSet:
    print('Set : ', x)
for x in sampleDictionary:
    print('Dictionary : ', x)
    
#배열합 구하기
sumx = 0
for x in [1, 2, 3, 4, 5]:
    sumx += x
print("sumx = ", sumx)