# 사용자가 입력한 상품 가격에 따라 할인율 적용 
# 상품 가격 입력  
price = int(input('상품 가격을 입력하세요 : '))
# 가격에 따라 할인율 적용 
if price >= 100000 :
    print('할인율 : 10%')
    print(f'할인 금액 : {int(price * 0.1)}원')
    print(f'최종 결제 금액 : {int(price - price * 0.1)}원')
elif price >= 50000 :
    print('할인율 : 5%')
    print(f'할인 금액 : {int(price * 0.05)}원')
    print(f'최종 결제 금액 : {int(price - price * 0.05)}원')
else :
    print('할인 없음')
    print(f'최종 결제 금액 : {price}원')
# 입력한 가격에 맞는 할인 금액 출력 

# 학점 판정기 만들기 
# 국어, 영어, 수학 점수를 입력 
input_value1 = int(input('국어 점수 입력 : '))
input_value2 = int(input('영어 점수 입력 : '))
input_value3 = int(input('수학 점수 입력 : '))
# 평균 점수 계산 
average = (input_value1 + input_value2 + input_value3) / 3 
print(f'평균 : {average:.1f}점') # 소수점 뒤의 길이를 제한하려면 :.숫자f 이런식으로 숫자 변수 뒤에 입력한다.
if input_value1 and input_value2 and input_value3 > 80 : 
    if average >= 90 :
        result = '결과 : 우수 합격'
elif input_value1 and input_value2 and input_value3 > 40 :
    if average >= 70 :
        result = '결과 : 합격'
else : 
    result = '결과 : 불합격'
print(result)