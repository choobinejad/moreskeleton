from datetime import datetime


class Double(object):
    def __init__(self):
        print('model')
        self.created = str(datetime.utcnow())
