# 비밀번호 검증기 만들기, 비밀번호를 입력하기
password = (input('비밀번호를 입력하세요 : '))
# 함수 박스를 만들어서 비밀번호의 규칙을 정하자 
def himitsu(password) :
    # 만약 비밀번호의 길이가 8자 이하인 경우 비밀번호가 짧음 
    if len(password) < 8 :
        return '비밀번호가 짧습니다.'
    # 만약 비밀번호에 하나 이상의 숫자라도 없을 경우 안전하지 않은 비밀번호, 하나 이상의 숫자라도 있으면 안전함 
    if not any(suuji.isdigit() for suuji in password) : 
        return '안전하지 않은 비밀번호입니다.'
    # 만약 비밀번호에 대문자가 하나라도 없을 경우 안전하지 않은 비번 
    if not any(moji.isupper() for moji in password) :
        return '안전하지 않은 비밀번호입니다.'
    # 만약 위의 명령문이 모두 반대로 될 경우에는 
    else :
        return '비밀번호가 안전합니다.'
print(himitsu(password))
    
    
