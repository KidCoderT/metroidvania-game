import csv
import pygame
from .spritesheets import SpriteSheet

mossy_tileset = SpriteSheet((512, 512), "./assets/tilemap/Mossy Tileset/Mossy - TileSet.png", (128, 128))
tile_size = 64

class MapLoader:
    def __init__(self, level: int = 1):
        self.level_number = level
        self.load_files()
        
        self.surface = pygame.Surface((self.width * 128, self.height * 128), pygame.SRCALPHA)
        self.load_tiles()
    
    def load_files(self):
        with open(f"./assets/map/{self.level_number}/map{self.level_number}_level.csv", encoding="utf-8") as file:
            level_reader = csv.reader(file, delimiter=",")
            self.level = list(level_reader)
            self.height = len(self.level)
            self.width = len(self.level[0])
        # Load LAVA & Player Pos
    
    def load_tiles(self):
        for j, row in enumerate(self.level):
            for i, cell in enumerate(row):
                if int(cell) == -1:
                    continue

                self.surface.blit(mossy_tileset[int(cell)], (i * tile_size, j * tile_size))
