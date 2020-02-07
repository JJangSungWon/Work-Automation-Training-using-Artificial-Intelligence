#들여쓰기(Python은 들여쓰기(intend)로 함수의 범위를 정한다.)
#스페이스 4번으로 구분한다.
def printnum():
    print('1')
    print('2')
print('3')
printnum()

#전역변수(global)
a = 100
print(a)
def f():
    global a
    a = a + 1
f()
print(a)