#while

#while 무한반복 True 등으로 가능
a = 1
while True:
    print(a)
    a += 1
    if a == 9:
        break

a = 1
while a < 3:
    print(a)
    a += 1
    if a == 5:
        break
else:
    print('good job') # if문을 통과하면 else는 실행 안됨.
    
    