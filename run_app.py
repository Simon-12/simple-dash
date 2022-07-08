import webbrowser
from app import app
from threading import Timer


def open_browser():
    webbrowser.get('windows-default').open('http://localhost:8050', new=2)


if __name__ == '__main__':
    Timer(2, open_browser).start()
    app.run_server()
