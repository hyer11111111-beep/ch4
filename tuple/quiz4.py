temp = ('bird','cat','dog')
b,c,d = temp
print(b,c,d)

# 변수 여러개 = 튜플
# 튜플의 요소가 순차적으로 변수에 저장됨
b,c,d = temp
print(b,c,d)

fruits = ('사과','배','포도','귤','딸기')
          
# 변수를 나열할때 , 나머지 변수는 항상 맨지막에
# 여러변수 , 나머지변수 = 튜플

a, *rest = fruits
print(a)
print(rest)
print(rest)
