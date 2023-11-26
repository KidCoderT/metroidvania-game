import pygame

from scripts.utils import setup_img
from .types import Size, Image


class SpriteSheet:
    def __init__(self, tile_size: Size, img: Image, scale: float = 1.0):
        self.img: pygame.SurfaceType = setup_img(img)

        self.scale = scale

        assert (
            self.img.get_width() % tile_size[0]
            == self.img.get_height() % tile_size[1]
            == 0
        )

        self.no_of_tiles_x = self.img.get_height() // tile_size[0]
        self.no_of_tiles_y = self.img.get_height() // tile_size[1]

        self.tile_size = tile_size
        self.tiles = []

        self.scale_and_cut_img()

    def scale_and_cut_img(self):
        self.scaled_img = pygame.transform.scale(
            self.img,
            (
                self.img.get_width() * self.scale,
                self.img.get_height() * self.scale,
            ),
        )

        self.tiles = []

        for j in range(self.no_of_tiles_y):
            for i in range(self.no_of_tiles_x):
                x = i * self.tile_size[0] * self.scale
                y = j * self.tile_size[1] * self.scale

                tile = pygame.Surface(self.tile_size)
                tile.blit(self.img, (x, y))
                self.tiles.append(tile)


class Animation:
    def __init__(self, frames: list[pygame.SurfaceType], duration, loop=True):
        self.tick = 0
        self.anim_inc = duration / len(frames)
        self.frames = frames
        self.loop = loop
        self.done = False

    def update(self):
        if self.loop:
            self.tick += self.anim_inc

        if int(self.tick) > len(self.frames):
            if not self.loop:
                self.done = True
            self.tick = 0

    def img(self):
        return self.frames[int(self.tick)]

    def reset(self):
        self.done = False
        self.tick = 0


class AnimatedSpritesheet(Animation):
    def __init__(
        self,
        tile_size: Size,
        img_path: str,
        scale: float = 1.0,
        duration=3,
        loop=True,
    ):
        self.spritesheet = SpriteSheet(tile_size, img_path, scale)
        super().__init__(self.spritesheet.tiles, duration, loop)
