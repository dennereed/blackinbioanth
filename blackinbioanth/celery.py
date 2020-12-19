"""
Celery config for blackinbioanth project.

For more information on this file, see
http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html

Run your celery worker(s) as `djcelery`, which is an alias for
`celery -A blackinbioanth worker --loglevel=info`.

A celerybeat scheduler can be started together with a worker by `djcelery -B`
or as a separate process:
`celery -A blackinbioanth beat
--loglevel=info -s /tmp/celerybeat-schedule`.
It needs to store the last run times of the tasks in a local database file:
if no -s option is provided it defaults to the cwd.
On production it shouldn't be in /tmp/.

"""

from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "blackinbioanth.settings.production")

app = Celery("blackinbioanth")

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
