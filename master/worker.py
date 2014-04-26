# -*- coding: utf-8 -*-

from celery import Celery

from config import CELERY_MASTER_BROKER


instance = Celery('master',
                  broker=CELERY_MASTER_BROKER)