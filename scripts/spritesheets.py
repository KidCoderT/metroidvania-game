import pygame

from scripts.utils import setup_img
from .types import Size, Image


class SpriteSheet:
    def __init__(self, tile_size: Size, img: Image, scale: float = 1.0):
        self.img: pygame.SurfaceType = setup_img(img)

        assert (
            self.img.get_width() % tile_size[0]
            == self.img.get_height() % tile_size[1]
            == 0
        )

        self.no_of_tiles_x = self.img.get_width() // tile_size[0]
        self.no_of_tiles_y = self.img.get_height() // tile_size[1]

        self.scale = scale
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

        tiles = []

        for j in range(self.no_of_tiles_y):
            for i in range(self.no_of_tiles_x):
                x = i * self.tile_size[0] * self.scale
                y = j * self.tile_size[1] * self.scale

                tile = pygame.Surface(
                    (
                        self.tile_size[0] * self.scale,
                        self.tile_size[1] * self.scale,
                    )
                )
                tile.blit(self.scaled_img, (-x, -y))
                tiles.append(tile)

        self.tiles = tiles

    def __getitem__(self, index) -> pygame.SurfaceType:
        return self.tiles[index]

    @property
    def width(self):
        return self.tile_size[0] * self.scale

    @property
    def height(self):
        return self.tile_size[1] * self.scale


class Animation:
    def __init__(self, frames: list[pygame.SurfaceType], duration=3, loop=True):
        self.current_frame = 0
        self.anim_duration = duration
        self.frames = frames
        self.loop = loop
        self.done = False

    def update(self):
        if self.loop:
            self.current_frame = (self.current_frame + 1) % (
                self.anim_duration * len(self.frames)
            )
            return

        self.frame = min(
            self.current_frame + 1, self.anim_duration * len(self.frames) - 1
        )
        if self.current_frame >= self.anim_duration * len(self.frames) - 1:
            self.done = True

    def img(self):
        return self.frames[int(self.current_frame / self.anim_duration)]

    def reset(self):
        self.current_frame = 0
        self.done = False


class AnimatedSpritesheet(Animation):
    def __init__(
        self,
        tile_size: Size,
        img: Image,
        scale: float = 1.0,
        duration: float | int = 3,
        loop=True,
    ):
        self.spritesheet = SpriteSheet(tile_size, img, scale)
        super().__init__(self.spritesheet.tiles, duration, loop)
