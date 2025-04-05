# 평균속도 계산기 만들기, 출발 시분 도착 시분 이동거리 입력하기 
Departure_hour = int(input('출발 시 (시간)을 입력하세요 : '))
Departure_minute = int(input('출발 시 (분)을 입력하세요 : '))
Arrival_hour = int(input('도착 시 (시간)을 입력하세요 : '))
Arrival_minute = int(input('도착 시 (분)을 입력하세요 : '))
travle_distance = float(input('이동 거리(km)를 입력하세요 : ')) 

# 평균 속도를 계산, 평균 속도 = 이동 거리 / 총 이동 시간, 총 이동 시간은 분 단위로 환산할 것 
total_travle_time = ((Arrival_hour * 60 + Arrival_minute) - (Departure_hour * 60 + Departure_minute) ) / 60 
average_speed = travle_distance / total_travle_time
# 이동 거리, 출발 시와 분, 도착 시와 분을 출력하고 평균 속도도 
print(f'이동 거리 : {travle_distance}km') 
print(f'출발 시간 : {Departure_hour}시 {Departure_minute}분')
print(f'도착 시간 : {Arrival_hour}시 {Arrival_minute}분')
print(f'평균 속도 : {average_speed :.2f}km/h')
# 평균 속도에 따라 빠름 느림 보통 나누기 
if average_speed < 60 :
    print('속도 상태 : 느림')
elif 60 <= average_speed < 90 :
    print('속도 상태 : 보통')
else : 
    print('속도 상태 : 빠름')

