# 별 패턴 그리기 (상승과 하강) 숫자를 입력하자
suuji = int(input('N 입력 : '))

# for 루프를 활용하여 별이 밑으로 나열되게 하기, 그리고 range() 함수를 사용해서 1부터 suuji 줄까지 나열되게 하자
for suuji in range(1, suuji + 1) : 
    print('*' * suuji) # suuji가 1부터 1씩 증가할 수록 곱하기도 1부터 1씩증가하기 때문에 '*' * suuji를 하여(suuji도 곱하기이기 때문에) 별이 차례대로 증가하게 한다.
# for 루프를 똑같이 써서 아래로 -1씩 나열되게 한다.
for suuji in range(suuji - 1, 0, -1) : # 스텝 값 -1 을 써서 suuji - 1 부터 0까지 1씩 감소하게 하기 
    print('*' * suuji) # 똑같이 suuji가 - 1부터 1씩 감소하므로 곱하기suuji도 1씩 감소한다.

