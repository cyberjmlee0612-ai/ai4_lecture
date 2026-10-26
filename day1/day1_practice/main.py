"""실습 메뉴 실행 파일.

상위 폴더에서 실행: python -m day1_practice
파일로 직접 실행: python day1_practice/main.py
이 폴더 안에서 실행: python main.py
"""

# 패키지 실행과 파일 직접 실행 모두 지원합니다.
if __package__:
    from .exercises.variables import practice_1
    from .exercises.conditions import practice_2
    from .exercises.lists import practice_3
    from .exercises.multiplication import practice_4
    from .exercises.number_game import practice_5
else:
    from day1.day1_practice.exercises.variables import practice_1
    from day1.day1_practice.exercises.conditions import practice_2
    from day1.day1_practice.exercises.lists import practice_3
    from day1.day1_practice.exercises.multiplication import practice_4
    from day1.day1_practice.exercises.number_game import practice_5


def main():
    """메뉴에서 선택한 실습을 실행하고 다시 메뉴로 돌아옵니다."""
    exercises = {
        "1": practice_1,
        "2": practice_2,
        "3": practice_3,
        "4": practice_4,
        "5": practice_5,
    }

    while True:
        print("\n=== Python 1일 차 복습 ===")
        print("1. 변수와 덧셈")
        print("2. 점수와 조건문")
        print("3. 리스트와 짝수 찾기")
        print("4. 중첩 반복문과 구구단")
        print("5. 숫자 맞추기 게임")
        print("0. 종료")
        choice = input("실습 번호를 선택하세요: ").strip()

        if choice == "0":
            print("실습을 종료합니다.")
            break
        if choice not in exercises:
            print("0~5 중에서 선택하세요.")
            continue

        exercise = exercises[choice]
        print(f"\n{exercise.__doc__.strip()}\n")
        try:
            exercise()
        except ValueError:
            print("정수를 입력해야 합니다. 메뉴에서 실습을 다시 선택하세요.")



if __name__ == "__main__":
    main()
