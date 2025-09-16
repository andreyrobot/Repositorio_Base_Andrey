import pygame
import sys

pygame.init()

# --- Configurações ---
WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Luta 2D")

FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (65, 105, 225)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
PURPLE = (128, 0, 128)

GROUND_Y = HEIGHT - 60

# --- Classes ---

class Platform:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GREY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Knife:
    def __init__(self, x, y, going_right):
        self.width = 30
        self.height = 10
        self.color = GREY
        self.speed = 15
        self.going_right = going_right
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = True

    def update(self):
        self.x += self.speed if self.going_right else -self.speed
        self.rect.x = self.x
        if self.x > WIDTH or self.x < -self.width:
            self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Weapon:
    def __init__(self, x, y):
        self.width = 30
        self.height = 30
        self.color = ORANGE
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.active = True

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect)


class Fighter:
    def __init__(self, x, y, color, controls, platforms):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.color = color
        self.speed = 5
        self.vel_y = 0
        self.jump_power = 15
        self.gravity = 1
        self.is_jumping = False

        self.health = 100
        self.max_health = 100

        self.attack_cooldown = 0
        self.attack_cooldown_max = 30
        self.is_attacking = False
        self.attack_box = None

        self.special_cooldown = 0
        self.special_cooldown_max = FPS * 5
        self.special_ready = True
        self.knives = []
        self.special_damage = 15

        self.controls = controls
        self.facing_right = True

        self.platforms = platforms

        # Bloqueio
        self.is_blocking = False
        self.block_hits_left = 4
        self.block_broken = False
        self.block_break_timer = 0
        self.block_break_duration = FPS * 2
        self.block_regen_timer = 0
        self.block_regen_cooldown = FPS * 3

        # Buff de arma
        self.weapon_buff = False
        self.buff_timer = 0
        self.buff_duration = FPS * 5
        self.buff_damage_bonus = 3

    def draw(self, surface):
        # Cor muda se bloqueando, quebrado ou buffado
        if self.weapon_buff:
            color = ORANGE
        elif self.block_broken:
            color = GREY
        elif self.is_blocking:
            # Cor mais escura no bloqueio
            color = (max(self.color[0] - 50, 0), max(self.color[1] - 50, 0), max(self.color[2] - 50, 0))
        else:
            color = self.color

        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))

        # Barra de vida
        health_ratio = self.health / self.max_health
        pygame.draw.rect(surface, RED, (self.x, self.y - 20, 100, 10))
        pygame.draw.rect(surface, GREEN, (self.x, self.y - 20, 100 * health_ratio, 10))

        # Barra de bloqueio
        block_ratio = self.block_hits_left / 4
        if self.block_broken:
            pygame.draw.rect(surface, RED, (self.x, self.y - 35, 100, 6))
        else:
            pygame.draw.rect(surface, BLACK, (self.x, self.y - 35, 100, 6))
            pygame.draw.rect(surface, BLUE, (self.x, self.y - 35, 100 * block_ratio, 6))

        # Barra do especial
        if self.special_ready:
            pygame.draw.rect(surface, PURPLE, (self.x, self.y - 50, 100, 6))
        else:
            cooldown_ratio = 1 - self.special_cooldown / self.special_cooldown_max
            cooldown_ratio = max(0, cooldown_ratio)
            pygame.draw.rect(surface, (100, 0, 100), (self.x, self.y - 50, 100, 6))
            pygame.draw.rect(surface, PURPLE, (self.x, self.y - 50, 100 * cooldown_ratio, 6))

        # Ataque visível
        if self.is_attacking and self.attack_box:
            pygame.draw.rect(surface, YELLOW, self.attack_box)

        # Desenhar facas especiais
        for knife in self.knives:
            if knife.active:
                knife.draw(surface)

    def move(self, keys):
        # Movimenta para esquerda/direita
        if keys[self.controls['left']] and self.x > 0:
            self.x -= self.speed
            self.facing_right = False
        if keys[self.controls['right']] and self.x < WIDTH - self.width:
            self.x += self.speed
            self.facing_right = True

        # Pular
        if not self.is_jumping and keys[self.controls['jump']]:
            self.vel_y = -self.jump_power
            self.is_jumping = True

        # Bloquear se não quebrado
        if keys[self.controls['block']] and not self.block_broken:
            self.is_blocking = True
        else:
            self.is_blocking = False

    def apply_gravity(self):
        # Aplica gravidade e verifica colisão com chão e plataformas
        self.y += self.vel_y
        self.vel_y += self.gravity

        # Checa colisão com plataformas e chão
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        on_platform = False
        for plat in self.platforms:
            if player_rect.colliderect(plat.rect) and self.vel_y >= 0:
                # Verifica se está pousando no topo da plataforma
                if self.y + self.height <= plat.rect.y + self.vel_y:
                    self.y = plat.rect.y - self.height
                    self.vel_y = 0
                    self.is_jumping = False
                    on_platform = True

        # Se não está em nenhuma plataforma, verifica chão
        if not on_platform:
            if self.y >= GROUND_Y - self.height:
                self.y = GROUND_Y - self.height
                self.vel_y = 0
                self.is_jumping = False

    def attack(self):
        if self.attack_cooldown == 0:
            self.is_attacking = True
            self.attack_cooldown = self.attack_cooldown_max
            w, h = 30, 20
            if self.facing_right:
                attack_x = self.x + self.width
            else:
                attack_x = self.x - w
            attack_y = self.y + self.height // 2 - h // 2
            self.attack_box = pygame.Rect(attack_x, attack_y, w, h)

    def use_special(self):
        if self.special_ready and len(self.knives) == 0:
            knife_x = self.x + self.width if self.facing_right else self.x - 30
            knife_y = self.y + self.height // 2 - 5
            self.knives.append(Knife(knife_x, knife_y, self.facing_right))
            self.special_ready = False
            self.special_cooldown = self.special_cooldown_max

    def cooldowns(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.is_attacking = False
            self.attack_box = None

        if self.special_cooldown > 0:
            self.special_cooldown -= 1
        else:
            self.special_ready = True

        if self.block_broken:
            self.block_break_timer -= 1
            if self.block_break_timer <= 0:
                self.block_broken = False
                self.block_hits_left = 4
                self.block_regen_timer = 0

        # Regenerar bloqueio se não quebrado
        if not self.block_broken and self.block_hits_left < 4:
            if self.block_regen_timer > 0:
                self.block_regen_timer -= 1
            else:
                self.block_hits_left = 4

        # Buff de arma tempo
        if self.weapon_buff:
            self.buff_timer -= 1
            if self.buff_timer <= 0:
                self.weapon_buff = False

        # Atualiza facas
        for knife in self.knives:
            knife.update()
        # Remove facas inativas
        self.knives = [k for k in self.knives if k.active]

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def receive_punch(self, damage=10):
        dmg = damage
        if self.weapon_buff:
            dmg += self.buff_damage_bonus

        if self.is_blocking and not self.block_broken:
            self.block_hits_left -= 1
            self.block_regen_timer = self.block_regen_cooldown
            if self.block_hits_left <= 0:
                self.block_broken = True
                self.block_break_timer = self.block_break_duration
                self.is_blocking = False
            return False  # bloqueou, não toma dano
        else:
            self.health -= dmg
            if self.health < 0:
                self.health = 0
            return True  # tomou dano


# --- Função principal ---

def main():
    # Controles para os jogadores
    controls_p1 = {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w,
                   'attack': pygame.K_f, 'block': pygame.K_g, 'special': pygame.K_r}
    controls_p2 = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP,
                   'attack': pygame.K_KP1, 'block': pygame.K_KP2, 'special': pygame.K_KP3}

    # Plataformas
    platforms = [
        Platform(250, GROUND_Y - 100, 150, 20),
        Platform(500, GROUND_Y - 150, 180, 20),
        Platform(100, GROUND_Y - 200, 120, 20)
    ]

    player1 = Fighter(100, GROUND_Y - 100, BLUE, controls_p1, platforms)
    player2 = Fighter(600, GROUND_Y - 100, RED, controls_p2, platforms)

    # Armas no mapa posicionadas em cima das plataformas
    weapons_on_map = [
        Weapon(280, platforms[0].rect.y - 30, ),
        Weapon(540, platforms[1].rect.y - 30),
        Weapon(130, platforms[2].rect.y - 30)
    ]

    running = True
    while running:
        clock.tick(FPS)
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Movimentação
        player1.move(keys)
        player2.move(keys)

        # Ataques
        if keys[player1.controls['attack']]:
            player1.attack()
        if keys[player2.controls['attack']]:
            player2.attack()

        # Especial
        if keys[player1.controls['special']]:
            player1.use_special()
        if keys[player2.controls['special']]:
            player2.use_special()

        # Gravidade e colisão com plataformas e chão
        player1.apply_gravity()
        player2.apply_gravity()

        # Cooldowns
        player1.cooldowns()
        player2.cooldowns()

        # Checa ataque player1 em player2
        if player1.is_attacking and player1.attack_box and player1.attack_box.colliderect(player2.get_rect()):
            took_damage = player2.receive_punch(10)
            if took_damage:
                print("Player 2 tomou dano do Player 1!")
            else:
                print("Player 2 bloqueou o ataque!")

        # Checa ataque player2 em player1
        if player2.is_attacking and player2.attack_box and player2.attack_box.colliderect(player1.get_rect()):
            took_damage = player1.receive_punch(10)
            if took_damage:
                print("Player 1 tomou dano do Player 2!")
            else:
                print("Player 1 bloqueou o ataque!")

        # Checa facas especiais colidindo com inimigo
        for knife in player1.knives:
            if knife.active and knife.rect.colliderect(player2.get_rect()):
                player2.receive_punch(player1.special_damage)
                knife.active = False

        for knife in player2.knives:
            if knife.active and knife.rect.colliderect(player1.get_rect()):
                player1.receive_punch(player2.special_damage)