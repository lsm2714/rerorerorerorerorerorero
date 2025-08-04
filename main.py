food_dict = {} 
age_list = ['10대', '20대', '30대', '40대', '종료']

# 반복 설정 
while True : 
    age = input('당신의 나이대는? (10대/20대/30대/40대/종료): ')
    if age not in age_list : 
        print('잘못된 입력입니다. 다시 입력해 주세요.')
        continue
    if age == '종료' : 
        break
    food = input('가장 좋아하는 음식은 무엇인가요? ')
    # 딕셔너리 설정 
    if age not in food_dict : 
        food_dict[age] = {food : 1}
    else : 
        if food in food_dict[age] :
            food_dict[age][food] += 1
        else : 
            food_dict[age][food] = 1

if food_dict == {} :
    print('저장된 설문 결과가 없습니다.')
else : 
    print('\n--- 설문 결과 ---')
    for k1, v1 in food_dict.items() : 
        print(f'[{k1}]')
        for k2, v2 in v1.items() :
            print(f'{k2}: {v2}회')
             





            