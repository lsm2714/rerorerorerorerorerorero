def bar() :
    msg1 = '<< ' + name 

    msg2 = foo(msg1)
    msg2 += " "

    msg3 = pos(msg2)
    msg3 += " "

    return msg3

def foo(argF) :
    msg = argF + '님'
    return msg

def pos(argP) :
    msg = argP + '안녕하세요'
    return msg
name = '이승민'

result = bar()

print(result)

''' def bar() 함수 안에서 msg1 = '<< ' + name(이승민) 이 있으므로 msg1 = << 이승민이 됨.
아래에서 msg2 = foo(msg1) 가 있고 아래로 내려가 foo(argF) 함수가 있는데 이때 같은 함수 안에 있으므로
msg1 = argF와 같아진다. 그리고 이때 msg = argF + '님' 으로 인해 msg = << 이승민님 이 된다. 이후 return을 통해 msg가 argF가 되므로
argF = msg1 이니까 msg1이 << 이승민님이 됨. 위에 적었듯 msg2 = foo(msg1) 이므로 msg2 = msg1이 되고 msg2는 msg += " " 로 인해 << 이승민님 (공백)이 된다.
아래의 msg3으로 내려가서 pos(msg2)가 있는데 아래에 pos(argP) 함수가 있어서 msg2 = argP가 된다. pos(argP) 함수 안에서 msg = argP + '안녕하세요' 이므로
msg = <<< 이승민님 안녕하세요 가 되고 return을 이용해 msg가 argP로 간다. argP = msg2이고 msg3 = pos(msg2) 가 있기 때문에 msg2 = msg3 가 되고
msg3 += " "로 인해 안녕하세요 뒤에 공백이 생긴다. return 을 이용해 msg3의 값이 bar() 함수의 매개변수로 전달되므로
result = << 이승민님 안녕하세요
print(result)로 출력.''' # def bar() 함수 안에서 name이 있으므로 name 변수를 찾아야 하지만 함수 안에 없으므로 함수를 나가서 변수를 찾는다. 
# 스코프 체이닝이라고 한다.