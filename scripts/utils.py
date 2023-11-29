import pygame
from .types import Image, Size, Scale, number


def setup_img(img: Image) -> pygame.SurfaceType:
    if isinstance(img, str):
        return pygame.image.load(img).convert_alpha()

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

def get_scale_factor(og_size: Size, scale_to: number | Size) -> number:
    if isinstance(scale_to, tuple):
        assert scale_to[0] / og_size[0] == scale_to[1] / og_size[1]
        return scale_to[0] / og_size[0]
    
    return float(scale_to)
