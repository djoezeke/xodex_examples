from xodex.scenes import Scene
from xodex.objects.spritesheet import SheetAnimator

# from xodex.objects.animator import Animator


class MainScene(Scene):
    """MainScene"""

    def __init__(self):
        super().__init__()
        self._score = 30

    def _generate_objects_(self):
        text = self.get_object(object_name="XodexText")
        seperator = self.get_object(object_name="UISEPERATOR")

        hor = seperator(self.screen, length=720, orientation="horizontal")
        hor.place(y=280, x=0)

        vet = seperator(master=self.screen, length=560, orientation="vertical")
        vet.place(y=0, x=360)

        yield vet
        yield hor

        yield text("IRONMAN", (100, 20), color=(58, 141, 255))
        yield text("SPIDERMAN", (450, 20), color=(58, 141, 255))
        yield text("DR.STRANGE", (100, 300), color=(58, 141, 255))
        yield text("BLACK PANTHER", (450, 300), color=(58, 141, 255))

        yield SheetAnimator("assets/images/dead.png", 80, 64, pos=(140, 85))
        yield SheetAnimator("assets/images/idle.png", 64, 64, pos=(500, 80))
        yield SheetAnimator("assets/images/jump.png", 64, 64, pos=(140, 360))
        yield SheetAnimator("assets/images/run.png", 80, 64, pos=(500, 360))

        yield from self.buttons()

    def buttons(self):
        """buttons"""
        buttons = []

        button1 = self.object.UIBUTTON(
            self.screen, text="ENTER", command=self.playwithhero1
        )
        button1.place(x=140, y=180)
        buttons.append(button1)

        button2 = self.object.UIBUTTON(
            self.screen, text="ENTER", command=self.playwithhero2
        )
        button2.place(x=500, y=180)
        buttons.append(button2)

        button3 = self.object.UIBUTTON(
            self.screen, text="ENTER", command=self.playwithhero3
        )
        button3.place(x=140, y=450)
        buttons.append(button3)

        button4 = self.object.UIBUTTON(
            self.screen, text="ENTER", command=self.playwithhero4
        )
        button4.place(x=500, y=450)
        buttons.append(button4)

        return buttons

    def playwithhero1(self):
        """playwithhero1"""

    def playwithhero2(self):
        """playwithhero2"""

    def playwithhero3(self):
        """playwithhero3"""

    def playwithhero4(self):
        """playwithhero4"""
