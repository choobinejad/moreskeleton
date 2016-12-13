from moreskeleton.app import App
from moreskeleton.echo.model import *


@App.path(model=Echo, path='echo')
def echo_path(q):
    e = Echo()
    e.text = q
    return e

