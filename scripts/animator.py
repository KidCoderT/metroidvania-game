import pygame
from .spritesheets import SpriteSheet
from .types import Size, Image, number

class Animation:
    def __init__(self, frames: list[pygame.SurfaceType], duration: number, loop=True):
        self.ticks: number = 0
        self.anim_duration = duration
        self.frames = frames
        self.loop = loop
        self.done = False

    def update(self):
        if self.done:
            return
        
        if self.loop:
            self.ticks += self.anim_duration / len(self.frames)
            return

        if int(self.ticks) > len(self.frames):
            self.done = True

    def img(self):
        return self.frames[int(self.ticks) % len(self.frames)]

    def reset(self):
        self.done = False
        self.ticks = 0

    def set_duration(self, duration: number):
        self.anim_duration = duration

class AnimatedSpritesheet(Animation):
    def __init__(
        self,
        tile_size: Size,
        img: Image,
        scale: float = 1.0,
        duration: number = 3,
        loop=True,
    ):
        self.spritesheet = SpriteSheet(tile_size, img, scale)
        super().__init__(self.spritesheet.tiles, duration, loop)
