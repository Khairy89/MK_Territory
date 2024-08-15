"""07: Navigate to File

Jump to a file without using the Project Tool and your mouse.

- Navigate to File (Shift-Ctrl-N Win/Linux, Shift-Cmd-O macOS)

- Look for ``s01``...opens file with cursor on last location

- Look for `fo/mo` to get ``fortytwo/models.py``

- Look for ``poolm`` to look in dependencies

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
