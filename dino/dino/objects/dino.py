# from xodex.objects.objects import DrawableObject
from xodex.objects.animator import Animator


class DinoDuck(Animator):
    """Pipe Obstacle"""

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
    """Pipe Obstacle"""

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
    """Pipe Obstacle"""

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
    """Pipe Obstacle"""

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
