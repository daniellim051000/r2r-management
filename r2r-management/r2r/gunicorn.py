"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count
from os import environ

bind = "0.0.0.0:" + environ.get("PORT", "8000")
max_requests = 10000
worker_class = "gevent"
workers = cpu_count() * 2 + 1
accesslog = "-"
errorlog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
loglevel = "debug"
