# 출석 점수 프로그램 만들기
#주당 수업 시간, 결석 시간, 지각 횟수를 입력하자
jikann = int(input('주당 수업 시간을 입력하세요 : '))
seki = int(input('결석 시간을 입력하세요 : '))
jikoku = int(input('지각 횟수를 입력하세요 : '))

# 출석 점수 프로그램을 만들기 위해 함수 박스를 만들자
def tennsuu(jikann, seki, jikoku) :
    # 총 수업 시간 계산식을 쓰자. 주당 수업시간이니까 주에 1을 적자
    jikann = jikann / 1 * 15 
    # 지각 3회는 결석 1시간으로 처리하므로 jikoku가 3의 배수일 때마다 seki에 수가 추가되도록 한다.
    seki += jikoku // 3 # jikoku 뒤에 // 3 을 입력하면 3으로 나눈 몫을 jikoku에 넣는다. seki = seki + (jikoku // 3)
    # 출석점수를 sasa에 변수 선언한다.
    sasa = 20 - (20 * seki / jikann)
    # 결석시수가 총 수업 시간의 1/4를 초과할 경우 'F (학점 미부여)' 를 출력한다
    if seki > jikann * 1/4 :
        sasa = 'F (학점 미부여)'
    # susu에 문장을 적습니다. 
    susu = f'당신의 출석 점수는 {sasa}입니다.'
    return susu 
# 위에 있는 문장을 출력합니다.
print(tennsuu(jikann, seki, jikoku))
    