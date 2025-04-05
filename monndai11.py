# 입력한 길이에 맞게 랜덤 비밀번호 생성하기 
# import를 사용하여 random 모듈 가져오기 
import random

def generate_password(length) : 
    # 대문자, 소문자, 숫자를 포함하여 한 변수에 지정하기
    uppercase_letters = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    lowercase_letters = uppercase_letters.lower() 
    digit = '0123456789'
    all_characters = uppercase_letters + lowercase_letters + digit 
    # 입력한 값만큼 all_characters 에서 랜덤으로 하나씩 꺼내서 합하기 (대소문자와 숫자를 반드시 포함시키기 위해 while 반복문을 사용)
    while True :
        # 랜덤으로 더하기 
        password = "" 
        for _ in range(length) :
            password += random.choice(all_characters)
        # password에 대소문자와 숫자를 포함하게 하기
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        if has_upper and has_lower and has_digit :
            # 위 조건이 True일 경우 return으로 password를 반환
            return password 
# 길이 입력 
password = int(input('패스워드의 길이를 입력하세요 : '))
if password < 4 :
    print('4자리 이상 입력해주세요.')
    exit() 
print(generate_password(password))
print('이건 Github 테스트용')



















































# 패스워드 생성 프로그램 만들기, random 모듈을 사용해야 되므로 import로 모듈을 불러온다.
'''import random 
# 값을 받아 계산을 해야 하므로 함수를 선언하고 패스워드에는 반드시 대문자, 소문자, 숫자가 들어가야 하기 때문에 각각을 변수선언하고 문자열로 더하여 새로운 변수 생성
def generate_password(length) :
    # 대문자를 변수 선언 
    uppercase_letters = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    # 소문자를 변수 선언하려면 .lower() 함수를 이용하여 모든 문자를 소문자로 바꿔줄 것 
    lowercase_letters = uppercase_letters.lower() 
    # 숫자도 변수 선언해주고 다 한 변수에 저장하자 
    digits = '0123456789'
    all_characters = uppercase_letters + lowercase_letters + digits 
    
    # 입력한 숫자에 따라 비밀번호의 길이를 정하고 무작위로 출력하게 하기(하지만 반드시 대소문자와 숫자를 포함해야 함 하나라도 빠지면 안됨)
    while True : # while 반복문을 쓰고 조건을 True로 하여 루프를 빠져나갈 때까지 무한 반복하게 하기 
        # 입력한 숫자만큼 반복하여 비밀번호를 랜덤으로 조합하는 코드 만들기 
        password = "" 
        for _ in range(length) :
            password += random.choice(all_characters) 
        # 근데 대소문자와 숫자가 하나 이상은 들어가 있어야 하니까 any() 함수를 활용하여 조건 만들기 
        has_upper = any(up.isupper() for up in password) 
        has_lower = any(low.islower() for low in password)
        has_digit = any(digit.isdigit() for digit in password)
        if has_digit and has_upper and has_lower :
            # 위의 조건문이 True일 경우 return으로 루프 빠져나가면서 password를 위에 있는 generate_password()에 값을 반환 
            return password
# 길이를 입력하기 
password = int(input('랜덤으로 지정할 패스워드의 길이를 입력하세요 : '))
if password < 4 :
    print('4자리 이상으로 해주세요.')
    # 위가 출력될 경우 밑의 모든 실행 끊어버리기 
    exit() 
print(generate_password(password)) # generate_password(password)는 generate_password(length)와 같으므로 
# 출력이 되기 전에 함수에서 모든 과정을 거쳐 올바른 값이 출력되게 할 수 있다.'''

