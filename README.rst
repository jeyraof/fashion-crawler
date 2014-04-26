Help
----

For using this, locate your prompt at this repo. So if you use `ls` command, you can see `crawler` directory.

Now, you can using this as following bottom:

1. Run beat for collect article list and apply this to miner.

.. code-block:: console

    $ celery -A crawler.worker beat

2. Run worker for mining (= miner)

.. code-block:: console

    $ celery -A crawler.worker worker

Worker could be run parallel. So your worker could be multiple instances.