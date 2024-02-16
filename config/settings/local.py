from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='x$%fh80ih73nwrk6g&vqmq&k_iuc(i8)i@hlgp$lub%w@-yq+*')
DEBUG = env.bool('DJANGO_DEBUG', default=True)