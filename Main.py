import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
score = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 5
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)
font = pygame.font.SysFont(None, 36)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            exit()
    all_sprites.update()
    collided_enemies = pygame.sprite.spritecollide(player, enemy_sprites, True)
    for enemy in collided_enemies:
        score += 1
    screen.fill(WHITE)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)