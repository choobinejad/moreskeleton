from datetime import datetime


class Echo(object):
    def __init__(self):
        self.created = str(datetime.utcnow())
