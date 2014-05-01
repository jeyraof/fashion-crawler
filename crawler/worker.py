# -*- coding: utf-8 -*-

from celery import Celery
from datetime import timedelta
from .config import CELERY_BROKER_URI
from .database import instant_session, Cafe, CafeBoard, CafeArticle, get_or_create

instance = Celery('crawler',
                  broker=CELERY_BROKER_URI)
instance.conf.update(
    CELERYBEAT_SCHEDULE={
        'renew-article-list': {
            'task': 'crawler.worker.master',
            'schedule': timedelta(seconds=10),
        },
    },
)


@instance.task(queue='fashion')
def master():
    print 'call slave()'
    slave.delay()


@instance.task(queue='fashion')
def slave():
    save_article.delay()


@instance.task(queue='fashion')
def save_article():
    session = instant_session()
    # Act as db session
    session.remove()
