"""31: Run Single Test

Speed up testing by focusing on one test.

- Right-click in the ``test_03`` test body, gutter click, filename, etc.

- Makes a temporary run config

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App
from fortytwo.models import Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
