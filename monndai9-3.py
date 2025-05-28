import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

# 1. 상수 데이터 정의 
X = [
    # Cluster 0
    (2.0, 1.8), (1.8, 2.2), (2.2, 2.0), (1.9, 2.1), (2.1, 1.9),
    # Cluster 1
    (6.0, 2.1), (6.2, 1.8), (5.8, 2.0), (6.1, 2.2), (5.9, 1.9),
    # Cluster 2
    (2.0, 6.0), (2.2, 6.2), (1.8, 5.9), (2.1, 6.1), (1.9, 5.8),
    # Cluster 3
    (6.0, 6.0), (5.9, 6.2), (6.1, 5.8), (5.8, 5.9), (6.2, 6.1)
]

# 2. 각 점이 속한 군집 번호 정의 
cluster_labels = [0]*5 + [1]*5 + [2]*5 + [3]*5 

# 3. x좌표와 y좌표를 분리 
x = [pt[0] for pt in X]
y = [pt[1] for pt in X]

# 4. 색상 정의 
colors = [plt.cm.tab10(i) for i in range(4)]
custom_cmap = ListedColormap(colors)

# 5. 산점도 그리기 
plt.scatter(x, y, c=cluster_labels, cmap=custom_cmap, s=100, alpha=0.8)

# 7. 그래프 출력 
plt.show() 