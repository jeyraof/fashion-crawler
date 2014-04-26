# -*- coding: utf-8 -*-

## Global

IS_SLAVE = False    # if this is True, slave would be worker



## Master
CELERY_MASTER_BROKER = 'amqp:///'



## Slave
CELERY_SLAVE_BROKER = 'amqp:///'