# 리스트를 이용한 통계량 계산 
import random 

# 루트 계산을 위한 math 모듈 불러오기 
import math

# 리스트 개수 입력 
number = int(input('리스트 개수를 입력하세요 (5~20) : '))
if 5 > number or number > 20 :
    print('오류 : 리스트 개수는 5 이상 20 이하여야 합니다.') 
    exit() 

# 입력한 숫자에 따라 리스트 요소 개수 랜덤으로 생성 
list_number = [random.randint(1, 100) for _ in range(number)]

# 리스트 출력 
print(f'\n생성된 리스트 : {list_number}')
# 평균 구하기 
avg = sum(list_number) / len(list_number)
print(f'평균 : {avg:.1f}')
# 편차 구하기 (소수점 2자리 수까지 반올림)
dev = [round(i - avg, 2) for i in list_number]
print(f'편차 : {dev}')
# 분산 구하기 
dev_var = 0
for dev_x in dev :
    dev_var += (dev_x**2)
var = dev_var / len(list_number)
print(f'분산 : {round(var, 2)}')
# 표준 편차 구하기 
Standatd_dev = math.sqrt(var) # 루트 씌울라면 math.sqrt() 하면 됨 
print(f'표준 편차 : {round(Standatd_dev, 2)}')
