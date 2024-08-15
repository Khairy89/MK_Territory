"""05: Use Recent Files to Open Tool Window

From the Recent Files popup, open one of the IDE tool windows.

- Let's get to the Terminal, without mouse

- Recent Files (Ctrl-E or Cmd-E)

    - Left column shows tools, not files

- Use cursor

- Better: speed type

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
