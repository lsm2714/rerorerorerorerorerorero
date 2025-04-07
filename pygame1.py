# pygame 모듈 가져오기 
import pygame 

#pygame 사용을 위한 초기화 
pygame.init() 

# 창 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# RGE 색상 기준으로 사용할 색깔 정의. 참조 : https://www.w3schools.com/colors/colors_picker.asp
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =(0, 0, 255)

# 화면 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 백 그라운드 색깔 설정 
display_surface.fill(BLUE)

# line 함수를 이용하여 라인 그리기 
pygame.draw.line(display_surface, RED, (100, 100), (200, 200), 3)

# circule() 함수를 이용하여 하얀색으로 동그라미 그리기
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 3)

# Rectangle() 함수를 이용하여 녹색으로 네모칸 그리기
pygame.draw.rect(display_surface, GREEN, (300, 0, 100, 100), 3)

# 이름 설정 
pygame.display.set_caption('이승민ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')

# 화면 계속 유지하고 event type이 QUIT일 경우 종료
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    #디스플레이 업데이트 
    pygame.display.update() 

# 화면 종료 
pygame.quit()




