# -*- coding: utf-8 -*-

from celery import Celery

from config import CELERY_SLAVE_BROKER


instance = Celery('master',
                  broker=CELERY_SLAVE_BROKER)