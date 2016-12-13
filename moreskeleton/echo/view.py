from moreskeleton.echo.path import *


@App.json(model=Echo, request_method='GET')
def echo_view(self, request):
    return self.__dict__
