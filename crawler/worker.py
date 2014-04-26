# -*- coding: utf-8 -*-

from celery import Celery
from datetime import timedelta

from .config import CELERY_BROKER_URI

instance = Celery('crawler',
                  broker=CELERY_BROKER_URI)
instance.conf.update(
    CELERYBEAT_SCHEDULE={
        'add-every-30-seconds': {
            'task': 'crawler.worker.master',
            'schedule': timedelta(seconds=10),
        },
    },
)


@instance.task()
def master():
    print 'call slave()'
    slave.delay()


@instance.task()
def slave():
    print 'slave called.'