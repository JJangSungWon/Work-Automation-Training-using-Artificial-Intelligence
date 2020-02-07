bool1 = True
bool2 = False
x = 1
y = 0
print(bool1 and bool2)       # False
print(bool2 or bool1)        # Ture
print(bool1 and not bool2)   #True
print(not bool1)             #False
print(x and not y)           #True
print(not x)                 #False

# 아래는 True, False가 아니라 0, 1의 결과가 나왔다
# boolean 형이 아닌 두 가지를 and, or 연산할때는 0 또는 1의 결과가 나오는 것 같다.
print(x and y) 
print(y or x)