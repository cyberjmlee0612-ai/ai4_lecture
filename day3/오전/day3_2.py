class DigitalWallet:
    def __init__(self, owner: str, initial_balance: int = 0):
        self.owner = owner #같은 owner가 아닌 왼쪽은 객체 오른쪽은 변수(이코딩)
        self.__balance = 0 #외부에서 직접 호출할 수 없는 변수를 만들고 일반 변수를 통해서 내부에서 함수형태로 만들어줌
        self.balance = initial_balance # setter 검문소를 거쳐 안전하게 초기화
    @property #값을 읽어올 때
    def balance(self) -> int: #함수명 똑같이 만들어준다
            print("balance 출력 호출")
            return self.__balance
    @balance.setter
    def balance(self, amount: int) -> None:
        if amount < 0:
            print(f"[보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: {amount}원 -> 거부됨)")
            return
        self.__balance = amount 
    def deposit(self, amount: int) -> str:
        if amount <= 0:
            return "[오류] 입금액은 0원보다 커야 합니다."
        self.balance += amount
        return f"[{self.owner}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)"
    def __str__(self):
        # print('객체자체를 호출하면 이 함수가 실행됩니다')
        return f"owner : {self.owner} __balance : {self.__balance}"

    
wallet = DigitalWallet("이코딩", 10000)
print(wallet.deposit(5000))
wallet.balance = -99999 # 외부에서 불법 음수 대입 시도 -> setter가 즉시 차단!
print(f"최종 안전 잔액: {wallet.balance:,}원")


# wallet.__balance = 200 (값을 할당하는걸 허용함 (파이썬만 덮어쓰기 가능 / 외부에서 접근할 수는 없음))

# 실행 결과:
# [이코딩] 5,000원 입금 완료 (현재 잔액: 15,000원)
# [보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: -99999원 -> 거부됨)
# 최종 안전 잔액: 15,000원
