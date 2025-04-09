# pygame 모듈 불러오기 
import pygame

# 원활하 실행을 위해 pygame 초기화
pygame.init() 

# 창 크기 설정 후 화면에 적용하기 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('그린란드 이미지 집어넣기')

# 이미지 불러오기 
greenland_image = pygame.image.load('Greenland-Waved-Flag-icon.png')
greenland_rect = greenland_image.get_rect() 
greenland_rect.centerx = (WINDOW_WIDTH//2)
greenland_rect.bottom = (WINDOW_HEIGHT//2)

# 화면이 계속 출력될 수 있도록 while 반복문과 True 조건 달기 
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
    # 초당 프레임 추가 
    clock = pygame.time.Clock()
    
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and greenland_rect.left > 0:     # 위의 코드를 입력하고 어떠한 키를 입력할 때마다 이 코드로 인식을 하여 알맞은 실행을 한다.
       greenland_rect.x -= 5
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and greenland_rect.right < WINDOW_WIDTH:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
       greenland_rect.x += 5
    if (key[pygame.K_UP] or key[pygame.K_w]) and greenland_rect.top > 0:
       greenland_rect.y -= 5
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and greenland_rect.bottom < WINDOW_HEIGHT:
       greenland_rect.y += 5
       
    # 이미지가 겹쳐 보이지 않게 fill() 메서드 입력을 하여 원한는 색깔 집어넣기 
    # (이건 updata가 있기 때문에 매 순간마다 화면을 특정 색깔로 칠해준다.)
    display_surface.fill((0, 0, 0))
       
    # 이미지를 화면에 출력
    display_surface.blit(greenland_image, greenland_rect)
    pygame.display.update() 
    
    # 초당 프레임 설정 
    clock.tick(60)
            
# 원활한 종료를 위해 pygame.quit() 메서드 설정
pygame.quit() 