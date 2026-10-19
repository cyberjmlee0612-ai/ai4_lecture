"""실습 3 모듈: 기존 학습 설명과 추가 연습을 포함합니다."""

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

