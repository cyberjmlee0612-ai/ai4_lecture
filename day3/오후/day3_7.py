class Order:
    """주문 정보와 금액 계산 동작을 하나로 묶은 클래스.

    회원 유형: 0(일반), 1(5%), 2(10%), 3(20%).
    가격과 수량은 0 이상의 정수이며, 쿠폰은 YES 또는 NO를 받는다.
    회원 할인 → 소수점 버림 → 쿠폰 차감 → 최소 0원 순서로 계산한다.
    """

    # 변경: 모든 주문에 공통으로 사용하는 정책을 클래스 속성으로 모았다.
    DISCOUNT_PERCENT = {0: 0, 1: 5, 2: 10, 3: 20}
    COUPON_AMOUNT = 3000

    def __init__(self, u_type: int, price: int, qty: int, coupon: str):
        """객체 생성 시 입력을 검증하고, 해당 주문의 정보를 저장한다."""
        # 기존 함수의 입력 검증을 생성자로 이동했다.
        # bool은 int의 하위 타입이므로 type으로 정확히 검사한다.
        for name, value in (("u_type", u_type), ("price", price), ("qty", qty)):
            if type(value) is not int:
                raise TypeError(f"{name}은 정수여야 합니다.")

        if u_type not in self.DISCOUNT_PERCENT:
            raise ValueError("u_type은 0, 1, 2, 3 중 하나여야 합니다.")
        if price < 0 or qty < 0:
            raise ValueError("price와 qty는 0 이상이어야 합니다.")
        if not isinstance(coupon, str):
            raise TypeError("coupon은 문자열이어야 합니다.")

        normalized_coupon = coupon.strip().upper()
        if normalized_coupon not in ("YES", "NO"):
            raise ValueError("coupon은 YES 또는 NO여야 합니다.")

        # 변경: 함수의 매개변수를 각 객체의 인스턴스 속성으로 저장한다.
        # self는 현재 주문 객체를 뜻한다. 주문마다 서로 다른 정보를 가진다.
        # 밑줄은 클래스 내부에서 사용하는 속성이라는 관례이며 강제 접근 제한은 아니다.
        self._u_type = u_type
        self._price = price
        self._qty = qty
        self._has_coupon = normalized_coupon == "YES"

    def calculate_subtotal(self) -> int:
        """할인 전 주문 금액을 계산한다."""
        # 변경: 가격 × 수량 계산을 별도 메서드로 분리해 재사용할 수 있다.
        return self._price * self._qty

    def calculate_total(self) -> int:
        """객체에 저장된 주문 정보로 최종 결제 금액을 계산한다."""
        # 변경: 매개변수를 다시 받지 않고 self의 주문 정보를 이용한다.
        total = self.calculate_subtotal()
        discount = self.DISCOUNT_PERCENT[self._u_type]

        # 기존 수정본의 정수 연산과 소수점 버림 정책을 유지한다.
        total = total * (100 - discount) // 100
        if self._has_coupon:
            total -= self.COUPON_AMOUNT

        # total은 지역 변수이므로 여러 번 호출해도 할인이 누적되지 않는다.
        return max(total, 0)


if __name__ == "__main__":
    # 변경 전: result = calc_order_fixed(1, 100, 20, "yes")
    # 변경 후: 주문 객체를 생성한 다음, 객체의 계산 메서드를 호출한다.
    order = Order(1, 100, 20, "yes")
    print(f"할인 전 주문 금액: {order.calculate_subtotal()}원")
    print(f"최종 주문 금액: {order.calculate_total()}원")
