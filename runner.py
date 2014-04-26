# -*- coding: utf-8 -*-

from config import IS_SLAVE


if IS_SLAVE:
    from .master.worker import instance
else:
    from .slave.worker import instance

instance.conf.update()