import time

from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from watchdog.events import *

from utils.log import log
from makingsystem.settings import MEDIA_ROOT
from utils.image_uploadaliyun import Xfer

log.initLogConf()
LOG = logging.getLogger(__file__)


class MyHandler(FileSystemEventHandler):

    def __init__(self):
        self.xfer = Xfer()

    def on_any_event(self, event):
        if event.is_directory:
            is_d = 'directory'
        else:
            is_d = 'file'
        log_s = f'{event.event_type, is_d, event.src_path}'
        LOG.info(log_s)

    def on_created(self, event):
        if event.is_directory:
            return
        self.xfer.initAliyun()
        path = 'image/' + event.src_path
        self.xfer.upload(path)
        self.xfer.clearAliyun()

    def on_modified(self, event):
        self.on_created(event)

    def on_deleted(self, event):
        pass

    def on_moved(self, event):
        pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('----开始监控是否有测试图片上传----------------')
        path = MEDIA_ROOT + '/image/'
        observer = Observer()
        event_handler = MyHandler()
        observer.schedule(event_handler, path, True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
