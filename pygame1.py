# pygame모듈 가져오기 
import pygame 

# 파이게임 실행을 위한 초기화 
pygame.init() 

# 창 크기 설정 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300 

# 색깔 설정 후 선언 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# 창 화면에 띄우기 (크기 설정, 이름 설정)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('이승민ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')

# 화면에 색 칠하기 
display_surface.fill(BLUE)

# line 함수를 이용하여 라인 그리기 
pygame.draw.line(display_surface, RED, (150, 134), (20, 120), 3)

# circle 함수를 이용하여 원 그리기 
pygame.draw.circle(display_surface, BLACK, (WINDOW_WIDTH//3, WINDOW_HEIGHT//3), 60, 4)

# rectangle() 함수를 이용하여 네모칸 그리기
pygame.draw.rect(display_surface, GREEN, (450, 80, 100, 100), 3)

# 화면에 계속 띄우기 위해 while 반복문에 True 조건 달기 
running = True 
while running :
    # 만약 event type이 QUIT일 경우 화면이 종료됨
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
        pygame.display.update()

# 원활한 종료를 위해 pygame.quit() 입력
pygame.quit()
    

