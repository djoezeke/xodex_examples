from xodex.scenes import Scene
from xodex.objects.spritesheet import SheetAnimator

# from xodex.objects.animator import Animator


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self._score = 30

    def _generate_objects_(self):
        text = self.get_object(object_name="XodexText")

        yield text("Hello Image Scene", (100, 150))
        yield SheetAnimator("assets/images/dead.png", 80, 64)
