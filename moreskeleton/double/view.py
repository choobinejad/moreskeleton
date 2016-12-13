from moreskeleton.double.path import *


@App.json(model=Double, request_method='GET')
def double_view(self, request):
    print('view')
    return self.__dict__
