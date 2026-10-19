# 논리연산자
# 단락평가 Short-ciruit
def expensive_check():
    print("시간이 오래 걸리는 함수 실행")
    return True

is_active = False

if is_active or expensive_check(): 
    print('통과')
else:
    print('차단(expensive_check 실행 안됨)')

# None 값을 방어
user_profile = None
if user_profile is not None and user_profile.get('is_verifled'):
    print('인증된 사용자')
else:
    print('비인증된 사용자')
    