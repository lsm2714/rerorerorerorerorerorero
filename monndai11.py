# 입력한 길이에 맞는 랜덤 비밀번호 생성기 
# 랜덤 모듈 불러오기 
import random

# 함수 박스를 만들어 입력한 길이 가져오기 
def generate_password(lenght) :
    # 대문자, 소문자, 숫자 설정 
    uppercase_letters = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    lowercase_letters = uppercase_letters.lower() 
    digit = '1029384756' 
    # 다 섞기 
    all_characters = lowercase_letters + uppercase_letters + digit 
    
    # while 반복문에 True 조건을 적용하여 대소문자, 숫자가 모두 나올 때까지 반복하기 
    while True :
        # 입력한 길이에 따라 랜덤 초이스 반복 
        password = '' 
        for _ in range(lenght) :
            password += random.choice(all_characters) 
            
        # 대문자, 소문자, 숫자가 모두 포함될 경우 반복문 종료. any() 함수 사용 
        has_upper = any(PW.isupper() for PW in password)
        has_lower = any(PW.islower() for PW in password)
        has_digit = any(PW.isdigit() for PW in password)
        
        if has_digit and has_lower and has_upper :
            return password # return으로 반복문을 종료하고 password를 generate_password()에 저장 

# 길이 입력 
lenght = int(input('패스워드의 길이를 입력하세요 (4자리 이상) : '))
if lenght < 4 :
    print('4자리 이상을 입력하세요')
    exit() 
print(generate_password(lenght))












































