# pygame 모듈 불러오기 
import pygame

# 원활하 실행을 위해 pygame 초기화
pygame.init() 

# 창 크기 설정 후 화면에 적용하기 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('그린란드 이미지 집어넣기')

# 초당 프레임 설정
clock = pygame.time.Clock()

# 이미지 불러오기 
bird_image = pygame.image.load('birdie-icon.png')
bird_rect = bird_image.get_rect()
bird_rect.centerx = (WINDOW_WIDTH // 2)
bird_rect.bottom = (WINDOW_HEIGHT // 2)

# 코믹스 이미지 붙이고 설정 
comix_image = pygame.image.load('comix-icon.png')
comix_rect = comix_image.get_rect()
comix_rect.centerx = (WINDOW_WIDTH//2)
comix_rect.bottom = (WINDOW_HEIGHT//3)

# 화면에 출력할 텍스트 설정하기
system_font = pygame.font.SysFont('verdana', 30)
game_font = system_font.render('FIGHT!!!!', True, (0, 255, 140), (80, 140, 220))
game_font_rect = game_font.get_rect()
game_font_rect.center = (WINDOW_WIDTH//2, 100)

# 화면이 계속 출력될 수 있도록 while 반복문과 True 조건 달기 
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
    
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 
    
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and bird_rect.left > 0:
        bird_rect.x -= 5
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and bird_rect.right < WINDOW_WIDTH:
        bird_rect.x += 5
    if (key[pygame.K_UP] or key[pygame.K_w]) and bird_rect.top > 0:
        bird_rect.y -= 5
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and bird_rect.bottom < WINDOW_HEIGHT:
        bird_rect.y += 5
       
    # 캐릭터 충돌 이벤트 구현 
    if bird_rect.colliderect(comix_rect) :
      print('충돌!!!!!!!!!!!!!!!!!')
    # 이미지가 겹쳐 보이지 않게 fill() 메서드 입력을 하여 원한는 색깔 집어넣기 
    # (이건 updata가 있기 때문에 매 순간마다 화면을 특정 색깔로 칠해준다.)
    display_surface.fill((0, 0, 0))
       
    # 이미지와 텍스트를 화면에 출력 (이미지가 아래로 가게 순서 맞추기)
    display_surface.blit(bird_image, bird_rect) 
    display_surface.blit(comix_image, comix_rect)
    display_surface.blit(game_font, game_font_rect)
    pygame.display.update() 
    
    # 초당 프레임 적용 
    clock.tick(60) 

# 원활한 종료를 위해 pygame.quit() 메서드 설정
pygame.quit() 
