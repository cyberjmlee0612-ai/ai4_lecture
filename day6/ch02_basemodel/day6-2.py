# 필수/기본값, 모델 생성/검증
from pydantic import BaseModel, ValidationError

class Member(BaseModel):
    username: str
    age: int
    active: bool = True  # 기본값 True
    nickname: str | None = None  # 선택적 필드, 기본값 None

class MemberOut(Member):
    id: int

# if__name__ == "__main__":
# m = Member(username='홍길동', age=20, active=True, nickname=None)
# print(m.username)

def main() -> None:
    member = Member(username='lee', age=20) # 디폴트가 있어서 나머지는 생략 가능
    print(member)
    raw = {'username': 'kim', 'age': 34, 'active': False}
    parsed = Member.model_validate(raw)
    print(parsed, 'age 타입', type(parsed.age.__name__))
    print('nickname 기본값',parsed.nickname))

    # 필수 필드 누락
    # Member.model_validate({'username': 'Kim'})  # age 필수 필드 누락, ValidationError 발생

    try:
        Member(username='Kim',age=20)  # age 필수 필드 누락, ValidationError 발생
        # Member(username='Kim')  # age 필수 필드 누락, ValidationError 발생
        
        # memberout 객체생성
        memberout = MemberOut(id=1,username='lee',age=20)
        print(memberout)
    except ValidationError as e:
        print(e.errors()[0]['loc'], e.errors()[0]['type'])

if __name__ == "__main__":
        main()