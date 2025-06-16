"""hello project Main Game Loop"""

import os
from xodex.game.game import Game


if __name__ == "__main__":
    os.environ.setdefault("XODEX_SETTINGS_MODULE", "hello.hello.settings")
    game = Game()
    game.main_loop()
