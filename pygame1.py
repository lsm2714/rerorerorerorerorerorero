import pygame

# pygame을 사용하기 위한 초기화 
pygame.init() 

# 창 크기 설정 
WINDOW_WIDTH = 600 
WINDOW_HEIGHT = 300

# 창에 대한 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World!')

# 게임이 동작하는 동안 이벤트 
running = True 
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

pygame.quit()