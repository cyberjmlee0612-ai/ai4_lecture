# pydantic
# 데이터의 유효성 및 타입을 체크
# 기능이 구현되 클래스를 상속받아서 pydantic 클래스 또는 모델을 만들 수 있음

fron pydantic import BaseModel, ValidationError
일반 파이썬 클래스
class NomalClass:
    def __init__(self, name: str, age: int): #normal class('홍길동',20)  ->매개변수가 없는 생성자를 호출
        # 객체변수(인스턴스변수)
        self.name = name
        self.age = age

# user1 = NomalClass(age=20,name="홍길동")
# paras = {'name':'홍길동','age':20}

user1 = NomalClass(name='홍길동', age=20) # 가이드
print('일반클래스',user1.age)``
print('데이터 타입',type(user1.age))

# pydantic 클래스
class PydanticClass(BaseModel):
    name: str
    age: int    

    user2 = PydanticClass(name="홍길동", age=20) # 강제
    print('일반클래스',user1.age)
    print('데이터 타입',type(user1.age))

try:
    user3 = PydanticClass(name="홍길동", age='스무살') # 강제
    print('일반클래스',user1.age)
    print('데이터 타입',type(user1.age))
except ValidationError as e:
    print('에러',e)