from xodex.objects.image import MovingImage


class Cloud(MovingImage):
    """Game Background Clood"""

    def __init__(
        self, win_width: int, win_height: int, pos: tuple[int, int], speed: int
    ):
        super().__init__(
            "assets/images/Other/Cloud.png",
            pos=pos,
            win_width=win_width,
            win_height=win_height,
            speed=speed,
        )
        self.allow_y = False


class Track(MovingImage):
    """Game Floor Track"""

    def __init__(self, win_width: int, win_height: int):
        super().__init__(
            "assets/images/Other/Track.png",
            pos=(0, int(win_height * 0.7)),
            win_width=win_width,
            win_height=win_height,
            speed=3,
        )
        self.allow_y = False
