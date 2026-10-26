"""1부터 n까지 짝수의 합과 개수를 계산하는 실습.

실행: python even_sum_practice/main.py
"""


def calculate_even_sum_and_count(n):
    """짝수의 합과 개수를 {"Sum": 합, "Count": 개수}로 반환한다."""
    even_sum = 0
    even_count = 0

    if n < 1:
        return {"Sum": 0, "Count": 0}

    # range의 끝값은 포함되지 않으므로 n + 1까지 지정한다.
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
            even_count += 1

    return {"Sum": even_sum, "Count": even_count}


if __name__ == "__main__":
    try:
        n = int(input("정수 n을 입력하세요: "))
        print(calculate_even_sum_and_count(n))
    except ValueError:
        print("정수를 입력하세요.")
