"""Python 1일 차 복습: 변수, 조건문, 리스트, 반복문, 숫자 맞추기.

실행 방법
    python python_day1_practice.py

사용 방법
    1. 메뉴에서 실습 번호를 선택합니다.
    2. 실행 전에 해당 함수의 코드를 읽고 결과를 예상합니다.
    3. 결과를 확인한 뒤 각 함수의 '추가 연습'을 직접 수정해 봅니다.

외부 라이브러리 설치는 필요하지 않습니다.
"""

import random  # Python에 기본으로 포함된 표준 라이브러리


def practice_1():
    """실습 1: 변수와 덧셈 (원본: day1-1.py).

    목표: 변수에 정수를 저장하고 계산 결과를 출력한다.
    예상 결과: number1 + number2 = 300
    추가 연습: 두 값을 바꾸고 뺄셈, 곱셈, 나눗셈도 출력해 보세요.
    """
    number1 = 100
    number2 = 200

    # 따옴표 안의 내용은 문자열입니다. 계산식은 따옴표 밖에 씁니다.
    print("number1 + number2 =", number1 + number2)


def practice_2():
    """실습 2: 점수에 따른 조건문 (원본: day1-2.py).

    목표: input(), int(), 비교 연산자, if/else를 사용한다.
    확인: 59 입력 → 불합격 / 60 입력 → 합격
    추가 연습: 0~100 범위를 벗어난 점수는 오류 메시지를 출력해 보세요.
    """
    # input()은 문자열을 반환하므로 정수 비교 전에 int()로 변환합니다.
    score = int(input("점수를 입력하세요: "))

    # 원본의 scor 오타를 score로 수정했습니다.
    if score >= 60:
        print("합격")
    else:
        print("불합격")


def practice_3():
    """실습 3: 리스트에 저장하고 짝수 찾기 (원본: day1-3.py).

    목표: 리스트, append(), for, range(), 나머지 연산자 %를 사용한다.
    확인: 1, 2, 3, 4, 5를 차례로 입력 → 짝수 2, 4 출력
    추가 연습: 홀수만 출력하거나 입력한 숫자의 합계를 출력해 보세요.
    """
    scores = []

    # range(5)는 0, 1, 2, 3, 4를 생성합니다.
    for i in range(5):
        score = int(input(f"{i + 1}번째 숫자를 입력하세요: "))
        scores.append(score)

    print("리스트의 값:", scores)
    print("짝수:")
    for number in scores:
        # 2로 나눈 나머지가 0이면 짝수입니다. 0과 음수에도 적용됩니다.
        if number % 2 == 0:
            print(number)


def practice_4():
    """실습 4: 중첩 반복문으로 구구단 출력 (원본: day1-4.py).

    목표: 중첩 for문, f-string, end, 탭과 줄바꿈을 사용한다.
    확인: 첫 출력은 2~4단의 곱하는 수 1~4, 둘째는 2~9단의 1~4행.
    추가 연습: 곱하는 수를 9까지 출력하도록 range()를 수정해 보세요.
    """
    # range(2, 5)는 2, 3, 4입니다. 끝값 5는 포함하지 않습니다.
    print("[단별 출력: 2~4단, 곱하는 수 1~4]")
    for dan in range(2, 5):
        for i in range(1, 5):
            # f-string은 중괄호 안의 변수나 계산 결과를 문자열에 넣습니다.
            # end="\t"는 기본 줄바꿈 대신 탭으로 구분합니다.
            print(f"{dan} x {i} = {dan * i}", end="\t")
        print("\n================================")

    print("\n[가로 출력: 2~9단, 곱하는 수 1~4]")
    for i in range(1, 5):
        for dan in range(2, 10):
            print(f"{dan} x {i} = {dan * i}", end="\t")
        print()  # 한 행을 출력한 뒤 줄바꿈


def practice_5():
    """실습 5: 숫자 맞추기 게임 (원본: day1-5.py).

    목표: random.randint(), while, if/elif/else, +=, break를 사용한다.
    확인: 1~100 사이의 숫자를 입력하고 힌트에 따라 정답을 찾아보세요.
    추가 연습: 입력 범위를 검사하거나 시도 횟수를 7회로 제한해 보세요.
    """
    # randint(1, 100)은 양 끝값을 포함한 정수 하나를 무작위로 선택합니다.
    com_number = random.randint(1, 100)
    count = 0

    while True:
        user_number = int(input("1~100 사이의 숫자를 입력하세요: "))
        count += 1  # count = count + 1과 같은 의미

        if user_number > com_number:
            print("입력한 숫자가 정답보다 큽니다.")
        elif user_number < com_number:
            print("입력한 숫자가 정답보다 작습니다.")
        else:
            print(f"정답입니다! 총 시도 횟수: {count}")
            break  # 가장 가까운 반복문을 종료합니다.


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


# 이 파일을 직접 실행했을 때만 메뉴를 시작합니다.
if __name__ == "__main__":
    main()
