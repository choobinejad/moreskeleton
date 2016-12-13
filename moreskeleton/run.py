import waitress
from moreskeleton.app import App
import morepath


def run():
    morepath.autoscan()
    App.commit()
    waitress.serve(App())


