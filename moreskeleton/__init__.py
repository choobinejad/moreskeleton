import morepath
from moreskeleton.view import *
from moreskeleton.run import run
import threading
import time
from datetime import datetime


if __name__ == '__main__':

    service_thread = threading.Thread(target=run)
    service_thread.daemon = True
    service_thread.start()

    while True:
        time.sleep(60)
        print('running', datetime.utcnow(), service_thread.is_alive())