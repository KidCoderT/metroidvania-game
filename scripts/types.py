import pygame

number = int | float
Image = str | pygame.Surface
Position = Size = tuple[int, int]
Scale = number | Size

__all__ = [
    "Position",
    "Image",
    "number",
    "Size",
    "Scale",
]