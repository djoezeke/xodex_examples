import pygame
from pygame.event import Event
from xodex.scenes import Scene, SceneManager


class MainScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _generate_objects_(self):
        Track = self.object.Track
        Cloud = self.object.Cloud

        track = Track(self.width, self.height)
        cloud = Cloud(
            self.width, self.height, pos=(int(self.width * 0.8), int(50)), speed=3
        )
        cloud2 = Cloud(
            self.width, self.height, pos=(int(self.width * 0.27), int(80)), speed=2
        )
        cloud3 = Cloud(
            self.width, self.height, pos=(int(self.width * 0.5), int(130)), speed=4
        )

        yield cloud
        yield cloud2
        yield cloud3
        yield track

    def handle_scene(self, event: Event, *args, **kwargs) -> None:
        """
        Handle an event for all objects in the scene.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.entergame()
        super().handle_scene(event, *args, **kwargs)

    def entergame(self):
        """entergame"""
        SceneManager().reset("GameScene")
