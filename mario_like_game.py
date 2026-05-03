import pygame
import sys
from pygame.locals import *

# 1. CONFIGURAÇÕES E CONSTANTES
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
FPS = 60
GRAVITY = 0.8
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_JUMP_FORCE = 16
WORLD_WIDTH = 3000 # Tamanho de cada nível

# Cores
SKY = (135, 206, 235)
GREEN = (50, 200, 50)
GOLD = (255, 215, 0)
BLUE = (20, 20, 160)

# 2. CLASSES
class Camera:
    def __init__(self, width, height):
        self.offset = pygame.Vector2(0, 0)
        self.width = width

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)

    def update(self, target_rect):
        x = target_rect.centerx - SCREEN_WIDTH // 2
        x = max(0, min(x, self.width - SCREEN_WIDTH))
        self.offset.x = x

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

class Flag(pygame.sprite.Sprite):
    """ Objeto que representa o fim do nível """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((36, 48), pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (0, 12, 36, 36))
        pygame.draw.rect(self.image, (255, 205, 180), (8, 0, 20, 20))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def jump(self, platforms):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2
        if hits:
            self.vel.y = -PLAYER_JUMP_FORCE

    def update(self, platforms):
        self.acc = pygame.Vector2(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]: self.acc.x = -PLAYER_ACC
        if keys[K_RIGHT] or keys[K_d]: self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        
        # Horizontal
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.rect.x = int(self.pos.x)
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for p in hits:
            if self.vel.x > 0: self.rect.right = p.rect.left
            elif self.vel.x < 0: self.rect.left = p.rect.right
            self.pos.x = self.rect.x
            self.vel.x = 0

        # Vertical
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        self.rect.y = int(self.pos.y)
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for p in hits:
            if self.vel.y > 0:
                self.rect.bottom = p.rect.top
                self.vel.y = 0
            elif self.vel.y < 0:
                self.rect.top = p.rect.bottom
                self.vel.y = 0
            self.pos.y = self.rect.y

# 3. LÓGICA DE NÍVEIS
def get_level_data(level_number):
    """ Retorna as plataformas e a posição da bandeira de cada nível """
    platforms = []
    # Chão comum para todos
    platforms.append(Platform(0, 580, WORLD_WIDTH, 60))
    
    if level_number == 1:
        platforms += [Platform(400, 450, 200, 20), Platform(700, 320, 200, 20)]
        flag_pos = (2800, 520)
    elif level_number == 2:
        platforms += [Platform(300, 480, 150, 20), Platform(500, 380, 150, 20), Platform(800, 280, 150, 20)]
        flag_pos = (2800, 520)
    elif level_number == 3:
        # Nível com buracos (plataformas menores)
        platforms = [Platform(0, 580, 500, 60), Platform(700, 580, 500, 60), Platform(1400, 580, 1600, 60)]
        platforms += [Platform(550, 400, 100, 20), Platform(1250, 400, 100, 20)]
        flag_pos = (2800, 520)
    elif level_number == 4:
        # Escada para cima
        for i in range(10):
            platforms.append(Platform(200 + (i*200), 500 - (i*40), 150, 20))
        flag_pos = (2800, 150)
    elif level_number == 5:
        # Desafio final
        platforms += [Platform(300, 400, 50, 20), Platform(500, 300, 50, 20), Platform(700, 400, 50, 20), Platform(900, 300, 50, 20)]
        flag_pos = (2800, 520)
    
    return platforms, flag_pos

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("Arial", 30, True)

    nivel_atual = 1
    max_niveis = 5

    while nivel_atual <= max_niveis:
        # --- SETUP DO NÍVEL ---
        all_platforms = pygame.sprite.Group()
        flags = pygame.sprite.Group()
        
        data_p, data_f = get_level_data(nivel_atual)
        for p in data_p: all_platforms.add(p)
        
        goal = Flag(data_f[0], data_f[1])
        flags.add(goal)
        
        player = Player(100, 500)
        camera = Camera(WORLD_WIDTH, SCREEN_HEIGHT)
        
        rodando_nivel = True
        while rodando_nivel:
            clock.tick(FPS)
            
            # 1. EVENTOS
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        player.jump(all_platforms)

            # 2. ATUALIZAÇÕES
            player.update(all_platforms)
            camera.update(player.rect)

            # Verificar se tocou na bandeira (passou de nível)
            if pygame.sprite.spritecollide(player, flags, False):
                nivel_atual += 1
                rodando_nivel = False

            # Verificar se caiu no buraco
            if player.rect.top > SCREEN_HEIGHT:
                rodando_nivel = False # Reinicia o mesmo nível

            # 3. DESENHO
            screen.fill(SKY)
            for p in all_platforms:
                screen.blit(p.image, camera.apply(p.rect))
            for f in flags:
                screen.blit(f.image, camera.apply(f.rect))
            screen.blit(player.image, camera.apply(player.rect))
            
            # Texto do nível
            texto = fonte.render(f"NÍVEL: {nivel_atual}", True, (255, 255, 255))
            screen.blit(texto, (20, 20))

            pygame.display.flip()

    # TELA DE VITÓRIA
    screen.fill(GREEN)
    vitoria = fonte.render("PARABÉNS! VOCÊ ZEROU O JOGO!", True, (255, 255, 255))
    screen.blit(vitoria, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
    