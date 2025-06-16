def generate_profile(name, age, gender='미정', *interests, **metadata) :
    print(f'''[고객 프로필]
이름 : {name}
나이 : {age}
성별 : {gender}''')
    if interests :
        print('관심사: ', end='')
        for value in interests[:-1] :
            print(value, end=', ')
        print(interests[-1]) 
    if metadata :
        print('추가 정보: ', end='')
        list_kv = []
        for k, v in metadata.items() :
            kv = f'{k}={v}'
            list_kv.append(kv)
        print(', '.join(list_kv))

generate_profile('홍길동', 30)

generate_profile('지민', 26, '여성', *['여행', '사진', '독서'], job='디자이너', country='한국')