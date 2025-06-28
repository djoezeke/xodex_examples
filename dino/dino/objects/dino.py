import pygame
from xodex.objects.animator import Animator, Anime


class DinoDuck(Animator):
    """Dino Animator"""

    def __init__(self, x, y):
        duck = [
            "assets/images/Dino/DinoDuck1.png",
            "assets/images/Dino/DinoDuck2.png",
        ]
        super().__init__(
            duck,
            frame_duration=100,
            loop=True,
            pingpong=False,
            reverse=False,
            on_finish=None,
            pos=(x, y),
        )


class DinoJump(Animator):
    """Dino Animator"""

    def __init__(self, x, y):
        duck = [
            "assets/images/Dino/DinoJump.png",
        ]
        super().__init__(
            duck,
            frame_duration=100,
            loop=True,
            pingpong=False,
            reverse=False,
            on_finish=None,
            pos=(x, y),
        )


class DinoDead(Animator):
    """Dino Animator"""

    def __init__(self, x, y):
        duck = [
            "assets/images/Dino/DinoDead.png",
        ]
        super().__init__(
            duck,
            frame_duration=100,
            loop=True,
            pingpong=False,
            reverse=False,
            on_finish=None,
            pos=(x, y),
        )


class DinoRun(Animator):
    """Dino Animator"""

    def __init__(self, x, y):
        duck = [
            "assets/images/Dino/DinoRun1.png",
            "assets/images/Dino/DinoRun2.png",
        ]
        super().__init__(
            duck,
            frame_duration=100,
            loop=True,
            pingpong=False,
            reverse=False,
            on_finish=None,
            pos=(x, y),
        )


class Dino(Anime):
    """Dino"""

    def __init__(self, x: int, y: int, default="run"):
        animations = {
            "run": DinoRun(x, y),
            "dead": DinoDead(x, y),
            "jump": DinoJump(x, y),
            "duck": DinoDuck(x, y),
        }
        super().__init__(animations, default)
