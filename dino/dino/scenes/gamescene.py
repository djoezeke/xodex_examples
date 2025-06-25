import pygame
from pygame.event import Event
from xodex.scenes import Scene, SceneManager


class GameScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Cactuses = self.object.Cactuses
        self.catuses = Cactuses(self.width, self.height)

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
        yield self.catuses

    def gameover(self):
        """entergame"""
        SceneManager().append("OverScene", self.screen, self.score.score)

    def is_tap_event(self, event) -> bool:
        """
        Determine if the event is a flap/tap event.

        Args:
            event: Pygame event.

        Returns:
            bool: True if event is a tap/flap.
        """
        m_left, _, _ = pygame.mouse.get_pressed()
        space_or_up = event.type == pygame.KEYDOWN and (
            event.key == pygame.K_SPACE or event.key == pygame.K_UP
        )
        screen_tap = event.type == pygame.FINGERDOWN
        return m_left or space_or_up or screen_tap

    def handle_scene(self, event: Event, *args, **kwargs) -> None:
        """
        Handle an event for all objects in the scene.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        super().handle_scene(event, *args, **kwargs)

    def update_scene(self, deltatime: float, *args, **kwargs) -> None:
        """
        Update all objects in the scene, unless paused.

        Args:
            deltatime (float): Time since last update (ms).
        """
        super().update_scene(deltatime, *args, **kwargs)
