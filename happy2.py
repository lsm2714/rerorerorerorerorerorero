# 사전예약 시스템 시뮬레이터 만들기
# 나이, 이벤트 코드, 예약 날짜 입력
toshi = int(input('나이를 입력해 주세요 : '))
code = input('예약하려는 이벤트 코드를 입력해 주세요 : ')
yoyaku = int(input('원하시는예약 날짜를입력해 주세요 : '))
# 함수 박스를 만들어서 규칙 만들기
def shisutemu(toshi, code, yoyaku) :
    #예약 날짜가 1일부터 30일까지가 아닌 경우 잘못된 입력
    if not (1<= yoyaku <= 30) :
        return '잘못된 입력입니다. 프로그램을 종료합니다.'
    # E1 코드일 경우 18 이하면 나이 제한으로 인해 예약 불가능 
    if code == 'E1' :
        if toshi < 18 :
            return '나이 제한으로 인해 예약할 수 없습니다.'
        else :
            return '예약이 완료되었습니다.'
    # 만약 코드가 E2일 경우 나이 상관은 없지만 짝수 날짜 이외에는 예약 불가능 
    if code == 'E2' :
        if yoyaku % 2 != 0 :
            return '선택하신 날짜에는 예약할 수 없습니다.' 
        else :
            return '예약이 완료되었습니다.'
    # 만약 코드가 E3일 경우 16세 미만은 예약이 안되고 7의 배수 날짜가 아닌 경우에도 예약이 안됨 
    if code == 'E3' :
        if toshi < 16 :
            return '나이 제한으로 인해 예약할 수 없습니다.'
        elif yoyaku % 7 != 0 :
            return '선택하신 날짜에는 예약할 수 없습니다.'
        else :
            return '예약이 완료되었습니다.'
    # 위에 적은 것들이 반대로 될 경우 예약 완료 
    else :
        return '잘못된 입력입니다. 프로그램을 종료합니다.'
print(shisutemu(toshi, code, yoyaku)) 
        
        
    