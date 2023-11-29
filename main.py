import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))


from scripts.animator import AnimatedSpritesheet
from scripts.tiles import mossy_tileset, MapLoader

playing = True
clock = pygame.time.Clock()

map = MapLoader()

# fmt: off
player_assets = {
    "idle": AnimatedSpritesheet((48, 48), "./assets/player/idle.png", 2, 2),
    "run": AnimatedSpritesheet((48, 48), "./assets/player/run cycle 48x48.png", 3, 2.5),
    # "death": AnimatedSpritesheet((64, 64), "./assets/player/Player Death/Player Death 64x64.png", 1.75, 8),
    # "hurt": AnimatedSpritesheet((48, 48), "./assets/player/Player Hurt-Damaged/Player Hurt 48x48.png", 2, 5),
    # "roll": AnimatedSpritesheet((48, 48), "./assets/player/Player Roll/Player Roll 48x48.png", 2, 4.75),
    # "air_roll": AnimatedSpritesheet((48, 48), "./assets/player/Air Spin/player air spin 48x48.png", 2, 3),
    # "katana_attack": AnimatedSpritesheet((80, 64), "./assets/player/Player Katana Continuous Attack/player katana continuous attack 80x64.png", 1.75, 3),
    # "katana_run": AnimatedSpritesheet((48, 48), "./assets/player/Player Katana Run/player katana run 48x48.png", 2, 4),
    # "shooting": AnimatedSpritesheet((48, 48), "./assets/player/Player Shoot 2H/player shoot 2H 48x48.png", 2, 3),
}
# fmt: on

time_elapsed_since_last_action = 0

while playing:
    screen.fill((65,94,89))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break
    
    screen.blit(player_assets["run"].img(), (60, 60))
    player_assets["run"].update()
    # player_assets["run"].set_duration(speed)

    # screen.blit(mossy_tileset[1], (60, 400))
    # pygame.draw.rect(screen, (0, 0, 0), (60, 400, 128, 128))
    screen.blit(map.surface, (0, 0))

    pygame.display.update()
    time_elapsed_since_last_action += clock.tick(60)
