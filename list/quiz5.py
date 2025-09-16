shopping = ['우유','빵','달걀']

shopping.append('사과')
print(shopping)

shopping[2] , "치즈"
print(shopping)

del shopping[1]
print(shopping)

scores = [ 60,75,80,90]

scores.append(100)
print(scores)

scores[2] = 85
print(scores)

last = scores.pop()
print(scores,last)

animals = ['강아지','고양이','토끼','햄스터']

animals[1] = ('고슴도치')
print(animals)

del animals[0]
print(animals)

last = animals.pop()
print(animals,last)