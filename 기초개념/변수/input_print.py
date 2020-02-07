#input
age = input('age를 입력하세요.')
lastname = input('lastname을 입력하세요')
firstname = input('firstname을 입력하세요')

#print
age = 10
name = 'leehojun'

print('1. 제 이름은', name, '입니다. 제 나이는', age, '입니다')
print('2. 제 이름은 {}입니다. 제 나이는{}입니다.' .format(name,age))
print('3. 제 이름은 %s입니다. 제 나이는 %d입니다.' %(name, age))