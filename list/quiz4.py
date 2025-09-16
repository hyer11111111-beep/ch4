fruits = []

fruits.insert(0,"사과")
print(fruits)

fruits.insert(1,"바나나")
print(fruits)

fruits.append("포도")
print(fruits)

numbers = [10,20,30,40]
numbers[1] = 99
print(numbers)

animals = ['강아지','고양이','토끼']
del animals[0]
print(animals)

subjects = ['국어','영어','수학','과락']
del subjects[1]
print(subjects)

scores = [70,80,90,100]
last = scores.pop()
print(scores,last)