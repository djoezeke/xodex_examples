import random
from typing import List
from xodex.objects.image import Image
from xodex.objects.objects import DrawableObject


class Cactus(Image):
    """Pipe Obstacle"""

    def __init__(self, cactus_type, x):
        cactus_sprites = [
            [
                "assets/images/Cactus/LargeCactus1.png",
                "assets/images/Cactus/LargeCactus2.png",
                "assets/images/Cactus/LargeCactus3.png",
            ],
            [
                "assets/images/Cactus/SmallCactus1.png",
                "assets/images/Cactus/SmallCactus2.png",
                "assets/images/Cactus/SmallCactus3.png",
            ],
        ]
        if cactus_type == 1:
            y = 360
        else:
            y = 335
        super().__init__(random.choice(cactus_sprites[cactus_type]), (x, y))
        self.vel_x = -5

    @property
    def rect(self):
        return self._img_rect

    def perform_draw(self, surface, *args, **kwargs):
        self._img_rect.x += self.vel_x
        return super().perform_draw(surface, *args, **kwargs)


class Cactuses(DrawableObject):
    """Pipes"""

    cactuses: List[Cactus]

    def __init__(self, win_width, win_height) -> "Cactuses":
        self.width = win_width
        self.height = win_height
        self.cactuses = []
        self.top = 0
        self.cactus_gap = 120
        self.bottom = win_height * 0.79
        self.spawn_initial_cactus()

    def stop(self) -> None:
        """stop"""
        for cactus in self.cactuses:
            cactus.vel_x = 0

    def can_spawn_cactus(self) -> bool:
        """can_spawn_cactus"""
        last = self.cactuses[-1]
        if not last:
            return True
        return self.width - (last.rect.x + last.rect.width) > last.rect.width * 2.5

    def spawn_new_cactus(self):
        """spawn_new_cactus"""
        cactus = self.make_cactus()
        self.cactuses.append(cactus)

    def remove_old_cactus(self):
        """remove_old_cactus"""
        # remove first cactus if its out of the screen
        for cactus in self.cactuses:
            if cactus.rect.x < -cactus.rect.width:
                self.cactuses.remove(cactus)

    def spawn_initial_cactus(self):
        """spawn_initial_cactus"""

        cactus = self.make_cactus()
        cactus.rect.x = self.width + cactus.rect.width * 3
        self.cactuses.append(cactus)

        cactus = self.make_cactus()
        cactus.rect.x = self.width + cactus.rect.width * 3.6
        self.cactuses.append(cactus)

    def make_cactus(self):
        """returns a randomly generated cactus"""
        gap = random.randrange(0, int(self.width - self.cactus_gap))
        cactus_type = random.choice([0, 1])
        cactus = Cactus(cactus_type, self.width + gap)
        return cactus

    def perform_draw(self, surface, *args, **kwargs):
        if self.can_spawn_cactus():
            self.spawn_new_cactus()
        self.remove_old_cactus()

        for cactus in self.cactuses:
            cactus.perform_draw(surface, *args, **kwargs)
