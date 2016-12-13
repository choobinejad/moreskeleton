from moreskeleton.app import App
from moreskeleton.double.model import *


@App.path(model=Double, path='double')
def double_path(q):
    print('path')
    d = Double()
    d.text = q * 2
    return d

