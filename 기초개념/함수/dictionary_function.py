#dictionary

fruit_shop = {'apple':1000, 'melon':3000, 'banana':2000}
print(fruit_shop['apple'])

#값 변경하기
fruit_shop['apple'] = 2000
print(fruit_shop['apple'])

#값 추가하기
fruit_shop['mango'] = 5000
print(fruit_shop)

#값 삭제하기
del fruit_shop['apple']
print(fruit_shop)

#길이 알기
print(len(fruit_shop))

#딕셔너리의 내장함수
#copy
fruit_shop_jeju = fruit_shop.copy() #copy를 사용하면 독립적인 개체로 복사
fruit_shop['banana'] = 3000
print(fruit_shop_jeju)

#clear - 사전의 모든 내용 삭제
print(fruit_shop.clear())

#get - key값으로 value 값을 반환하는 함수
print(fruit_shop_jeju.get('banana'))

#update - 다른 사전의 내용을 합쳐주는 함수
fruit_shop={'apple':1000, 'melon':3000, 'banana':2000}
fruit_shop_jeju ={'apple':2000, 'pear':1500}
fruit_shop.update(fruit_shop_jeju)
print(fruit_shop)

#keys - dictionary의 key값만 모아서 list형태로 변환
print(fruit_shop.keys())

#values - dictionary의 value값만 모아서 list형태로 반환
print(fruit_shop.values())

#items - key:value의 형태를 튜플로 반환
print(fruit_shop.items())

#has_key - key값이 존재하는 지 여부를 파악 (python 3.대 버전부터 in으로 수정됨)
print('banana' in fruit_shop)
print('mango' in fruit_shop)



