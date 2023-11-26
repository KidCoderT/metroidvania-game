import pygame
from .types import Image


def setup_img(img: Image) -> pygame.SurfaceType:
    if isinstance(img, str):
        return pygame.image.load(img)

    return img.copy()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    img = pygame.transform.scale(img, size)
    img.convert()
    return img


def outline_mask(img, loc, display):
    mask = pygame.mask.from_surface(img)
    mask_outline = mask.outline()
    n = 0
    for point in mask_outline:
        mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
        n += 1
    pygame.draw.polygon(display, (255, 255, 255), mask_outline, 3)
