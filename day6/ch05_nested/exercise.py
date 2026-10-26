"""05장 학생 실습: 강좌와 수강생의 중첩 관계 모델링."""
from pydantic import BaseModel, Field


# BaseModel을 상속하면 입력값의 자료형과 조건을 검사할 수 있습니다.
class Learner(BaseModel):
    name: str
    # ge=0은 0 이상, le=100은 100 이하라는 뜻입니다.
    score: int = Field(ge=0, le=100)


class Course(BaseModel):
    title: str
    # 수강생마다 Learner의 조건을 검사하고, 최소 1명이 있는지도 확인합니다.
    learners: list[Learner] = Field(min_length=1)


def main() -> None:
    # 강좌 안에 수강생 정보가 들어 있는 딕셔너리입니다.
    data = {
        'title': '파이썬 기초',
        'learners': [
            {'name': '민수', 'score': 80},
            {'name': '지영', 'score': 95},
        ],
    }

    # 강좌와 수강생 정보를 함께 검사합니다.
    # 안쪽의 수강생 딕셔너리도 자동으로 Learner 객체가 됩니다.
    course = Course.model_validate(data)

    print('강좌 이름:', course.title)
    for learner in course.learners:
        print('이름:', learner.name, '점수:', learner.score)


if __name__ == '__main__':
    main()
