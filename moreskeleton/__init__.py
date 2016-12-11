import morepath
from moreskeleton.view import *
import threading
import time
from datetime import datetime


if __name__ == '__main__':

    service_thread = threading.Thread(target=morepath.run, args=[App()])
    service_thread.daemon = True
    service_thread.start()

    while True:
        time.sleep(60)
        print('running', datetime.utcnow(), service_thread.is_alive())