sampleList = [1,1,2,2,3,3,4,4,5,7,7,7,7,7,7]
sampleTuple = (1,2,3,4,5,7,7,7,7,7,7,7,7,7,7)
sampleSet = set(sampleList)
sampleDictionary ={'one':1,'two':2,'three':3}

maxList = max(sampleList)
maxTuple = max(sampleTuple)
maxSet = max(sampleSet)
maxDictionary = max(sampleDictionary)

minList = min(sampleList)
minTuple = min(sampleTuple)
minSet = min(sampleSet)
minDictionary = min(sampleDictionary)

print("max")
print("maxList:", maxList)
print("maxTuple:", maxTuple)
print("maxSet:", maxSet)
print("maxDictionary:", maxDictionary)

print("\nmin")
print("minList:", minList)
print("minTuple:", minTuple)
print("minSet:", minSet)
print("minDictionary:", minDictionary)

#swap
x = 10
y = 20

x,y = y,x
print(x, y)