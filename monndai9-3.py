list_int = []

print('정수 10개를 입력하세요.')
for num in range(1, 11) :
    int_value = int(input(f'{num}번째 정수 : '))
    # 리스트 안에 넣기 
    list_int.append(int_value)
    
# 원본 리스트 
print(f'''
[원본 리스트]
{list_int[:]}''')
# 처음 5개 원소 
print(f'''
1. 처음 5개 원소 :
{list_int[:5]}''')
# 뒤에서 3개 원소 
print(f'''
2. 뒤에서 3개 원소 :
{list_int[-3:]}''')
# 짝수 인덱스 원소 
print(f'''
3. 짝수 인덱스 원소 :
{list_int[::2]}''')
# 거꾸로 뒤집은 리스트  
print(f'''
4. 거꾸로 뒤집은 리스트 :
{list_int[::-1]}''')

