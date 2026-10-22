'''day6_2'''
# import day6_2

# member = day6_2.Member(username='홍길동', age=20, active=True, nickname=None)
# # if __name__ == "__main__":
# if member.age > 19:
#     print("성인입니다.")

# print(__name__)


'''day6_2ex'''

from pydantic import BaseModel, ValidationError


# 책 정보를 저장하는 모델
class Book(BaseModel):
    title: str             # 필수: 책 제목
    price: int              # 필수: 가격
    in_stock: bool = True   # 선택: 기본값은 True
    note: str | None = None # 선택: 문자열 또는 None


def main() -> None:
    # 1. 책 객체 생성
    book = Book(title='파이썬 기초', price='19000')
    print(book)

    # 2. 딕셔너리로 변환
    print(book.model_dump())

    # 3. 가격이 정수형으로 변환되었는지 확인
    # model_dump()를 호출하면, Pydantic은 문자열로 입력된 '19000'을 자동으로 정수형으로 변환합니다. <--? 가격이 int로 변환되었는지 확인
    print('가격:', book.price)
    print('가격의 타입:', type(book.price))

    # 4. 필수 항목인 title을 누락하면 어떻게 될까?
    try:
        Book(price=19000)
    except ValidationError as e:
        print('유효성 검사 오류:')
        print(e)


if __name__ == '__main__':
    main()
