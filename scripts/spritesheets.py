import pygame

from scripts.utils import setup_img, get_scale_factor
from .types import Size, Image, Scale


class SpriteSheet:
    def __init__(self, tile_size: Size, img: Image, scale: Scale):
        self.img: pygame.SurfaceType = setup_img(img)

        assert (
            self.img.get_width() % tile_size[0]
            == self.img.get_height() % tile_size[1]
            == 0
        )

        self.no_of_tiles_x = self.img.get_width() // tile_size[0]
        self.no_of_tiles_y = self.img.get_height() // tile_size[1]

        self.scale = get_scale_factor(tile_size, scale)
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
                , pygame.SRCALPHA)
                
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

