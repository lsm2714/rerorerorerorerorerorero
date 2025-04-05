def incrementCount() :
    global count 
    count = count + 3

def decrementCount() : 
    global count 
    count = count -2
    
count = 4
    
incrementCount()
print(count)

decrementCount() 
print(count)

incrementCount()
print(count)
decrementCount()
print(count)

''' global 함수를 썼으므로 함수 안의 변수와 밖의 변수가 같아짐. incrementCount() print(count) 로 count를 출력해야 하는데
count = 4 이고 def incrementCount() 함수 안에서 알고리즘을 거쳐 count = 7 이 된다. 처음으로 7이 출력되고 decrementCount() print(count)
로 이후 다음 count가 출력되야 됨 count = 7이고 def decrementCount() 함수에서 알고리즘을 거쳐 count = 5가 됨. 
이후 incrementCount() 함수로 count = 8이 되고 decrementCount() 함수로 - 2가 되어 6이 출력된다.
결과
7
5
8
6
'''