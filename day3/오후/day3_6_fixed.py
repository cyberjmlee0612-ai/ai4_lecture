def calc_order_fixed(u_type: int, price: int, qty: int, coupon: str) -> int:
    """회원 할인 후 쿠폰을 적용한 주문 금액을 정수로 반환한다.

    u_type: 0(일반), 1(5%), 2(10%), 3(20%)
    price, qty: 0 이상의 정수. 가격은 원 단위이며 수량 0도 허용한다.
    coupon: YES 또는 NO. 대소문자와 앞뒤 공백은 무시한다.
    할인 금액의 소수점 이하는 버리고, 최종 금액은 최소 0원이다.
    """
    # 수정: bool도 int의 하위 타입이므로 정확한 타입을 검사해 True 등을 거부한다.
    for name, value in (("u_type", u_type), ("price", price), ("qty", qty)):
        if type(value) is not int:
            raise TypeError(f"{name}은 정수여야 합니다.")

    # 수정: 일반 회원은 0으로 명시하고, 잘못된 회원 유형과 음수 입력을 거부한다.
    discount_percent = {0: 0, 1: 5, 2: 10, 3: 20}
    if u_type not in discount_percent:
        raise ValueError("u_type은 0, 1, 2, 3 중 하나여야 합니다.")
    if price < 0 or qty < 0:
        raise ValueError("price와 qty는 0 이상이어야 합니다.")

    # 수정: 문자열인지 먼저 확인하고 대소문자와 공백을 정리해 쿠폰을 판별한다.
    if not isinstance(coupon, str):
        raise TypeError("coupon은 문자열이어야 합니다.")
    normalized_coupon = coupon.strip().upper()
    if normalized_coupon not in ("YES", "NO"):
        raise ValueError("coupon은 YES 또는 NO여야 합니다.")

    # 수정: 정수 연산으로 부동소수점 오차를 없애고 기존 소수점 버림 정책을 유지한다.
    total = price * qty
    total = total * (100 - discount_percent[u_type]) // 100

    # 기존 정책 유지: 회원 할인을 먼저 적용하고 쿠폰 3,000원을 차감한다.
    if normalized_coupon == "YES":
        total -= 3000

    # 수정: 끝의 쉼표를 제거해 튜플 대신 정수를 반환한다. 최저 금액은 0원이다.
    return max(total, 0)


# 수정: 다른 파일에서 import할 때 예제 코드가 실행되지 않도록 분리한다.
if __name__ == "__main__":
    result = calc_order_fixed(1, 100, 20, "yes")
    print(f"최종 주문 금액: {result}원")
