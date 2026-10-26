"""실습 5 모듈: 기존 학습 설명과 추가 연습을 포함합니다."""

import random  # Python 표준 라이브러리


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

