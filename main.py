import pygame
import random

from scripts.spritesheets import AnimatedSpritesheet

pygame.init()

screen = pygame.display.set_mode((1000, 800))

playing = True
clock = pygame.time.Clock()

# fmt: off
player_assets = {
    "idle": AnimatedSpritesheet((48, 48), "./assets/player/idle.png", 2, 5),
    "run": AnimatedSpritesheet((48, 48), "./assets/player/run cycle 48x48.png", 2, 3.5),
    "death": AnimatedSpritesheet((64, 64), "./assets/player/Player Death/Player Death 64x64.png", 1.75, 8),
    "hurt": AnimatedSpritesheet((48, 48), "./assets/player/Player Hurt-Damaged/Player Hurt 48x48.png", 2, 5),
    "roll": AnimatedSpritesheet((48, 48), "./assets/player/Player Roll/Player Roll 48x48.png", 2, 4.75),
    "air_roll": AnimatedSpritesheet((48, 48), "./assets/player/Air Spin/player air spin 48x48.png", 2, 3),
    "katana_attack": AnimatedSpritesheet((80, 64), "./assets/player/Player Katana Continuous Attack/player katana continuous attack 80x64.png", 1.75, 3),
    "katana_run": AnimatedSpritesheet((48, 48), "./assets/player/Player Katana Run/player katana run 48x48.png", 2, 3),
    "shooting": AnimatedSpritesheet((48, 48), "./assets/player/Player Shoot 2H/player shoot 2H 48x48.png", 2, 3),
}
# fmt: on

while playing:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break

    y = 0
    for i, animator in enumerate(player_assets.values()):
        screen.blit(animator.img(), (150 * (i % 3) + 20, 120 * y + 20))
        animator.update()
        if i > 0 and i % 3 == 0:
            y += 1

    pygame.display.update()
    clock.tick(60)
