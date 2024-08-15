"""02: Reduce Clutter

Reduce Clutter by Disabling Tools.

- We are an IDE, but we can also do a lean-and-mean UI

- Hide the Toolbar, Tool Window Bars, Navigation Bar

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
