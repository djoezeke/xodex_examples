"""
Scene Registration for hello project.

Register your custom scenes here using the @register decorator.

Example:

Registering Scene On Creation.

    ```python
    from xodex.scenes.manager import register
    from xodex.scenes import Scene

    # Register a menu scene with default name (class name)
    @register
    class MenuScene(Scene):
        ...

    # Register a scene with a custom name
    @register(name="main_menu")
    class MenuScene(Scene):
        ...
    ```

Registering Existing Scene.

    ```python
    from xodex.scenes.manager import register
    from .menu_scene import MenuScene

    # Register a menu scene with default name (class name)
    register(MenuScene)

    # Register a scene with a custom name
    register(MenuScene,name="main_menu")
    ```

How it works:
- The @register decorator adds your scene class to the global registry.
- You can then instantiate or reference these scenes by name in your game flow.
- Use inheritance to create custom scene logic, transitions, and layouts.

See the Xodex documentation for more advanced scene management and transitions.
"""

from xodex.scenes.manager import register, SceneManager
from xodex.scenes import Scene

# Register your Scenes here.


# @register
class UIScene(Scene):
    """UIScene"""

    def __init__(self):
        super().__init__()

    def _generate_objects_(self):
        text = self.object.get_object(object_name="XodexText")
        label = self.object.get_object(object_name="UILABEL")
        btn = self.object.get_object(object_name="UIBTN")

        label1 = label(master=self._screen, text="My Label")
        label1.place(x=100, y=200)

        btn1 = btn(master=self._screen, text="Click Me")
        btn1.place(x=100, y=300)

        yield label1
        yield btn1

        yield text("Hello", (10, 100))


SceneManager().register(UIScene, name="UIScene")
