import matplotlib.pyplot as plt 

# 그래프 좌표 설정
x = [val for val in range(-10, 11)]
y1 = [val*2 for val in x]
y2 = [val*4 for val in x]
y3 = [val*6 for val in x]

# 그래프 그리기 
plt.plot(x, y1, label = 'X2')
plt.plot(x, y2, color = 'red', marker = 'o', label = 'X4')
plt.plot(x, y3, marker = 'x', label = 'X6')

# 그래프 꾸미기 
plt.legend() 
plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('GRAPH') 
plt.grid(True) # 그래프 바탕에 선 추가 

# 그래프 출력 
plt.show() 

