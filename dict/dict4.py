# 모듈 불러오기
# 모듈 : 특정 기능을 미리 만들어둔 파일
# 깊은 복사를 위해 모듈 불러오기
import copy


# 객체 복사하기

dic = {'name':'둘리', 'age':20 }
dic_copy = dic.copy()
print(dic_copy)

# 복사본의 내용 수정하기
# 복사본을 수정해도 원본에는 영향이 없다
# -> 완벽하게 복사됨
dic_copy ['age'] = 25
print('원본:',dic)
print('복사본:',dic_copy)

# 취미 추가 
dic = {'name':'둘리', 'age':20 ,"hobby":['축구','야구'] }
# 객체 복사하기
dic_copy = dic.copy()
# 복사본에서 취미 수정
# 축구 > 테니스 

# 복사본을 수정했는데 원본도 함께 수정됨 -> 얇은 복사
# hobby는 리스트이고 , 리스트의 값이 아닌 주소가 복사됨
# 따라서 원본과 복사본은 같은 리스트를 바라봄
dic_copy['hobby'][0] = '테니스'
print("원본:", dic)
print("복사본:", dic_copy)

#깊은복사
dic = {'name': '둘리', 'age': 10, 'hobby': ['축구','야구']}
dic_copy = copy.deepcopy(dic)

dic_copy['hobby'][0] = '테니스'
print("원본:", dic) 
print("복사본:", dic_copy)

