import pygame

# pygame을 사용하기 위한 초기화 
pygame.init() 

# 창 크기 설정 
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# 창에 대한 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('이미지 키보드 이벤트')

# 이미지 붙이고 설정 
Greenland_image = pygame.image.load('Greenland-waved-Flag-icon.png')
Greenland_rect = Greenland_image.get_rect()
Greenland_rect.centerx = (WINDOW_WIDTH//2)
Greenland_rect.bottom = (WINDOW_HEIGHT//2)

# 게임이 동작하는 동안 이벤트 
running = True 
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    # 키보트 이벤트 적용 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        Greenland_rect.x -= 1
    if keys[pygame.K_RIGHT]:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
        Greenland_rect.x += 1
    if keys[pygame.K_UP]:
        Greenland_rect.y -= 1
    if keys[pygame.K_DOWN]:
        Greenland_rect.y += 1
    
    display_surface.fill((0, 0, 0))
    # 이미지 출력 = blit(이미지 객체, 위치)
    display_surface.blit(Greenland_image, Greenland_rect)
    # 디스플레이 업데이트 
    pygame.display.update()

pygame.quit()