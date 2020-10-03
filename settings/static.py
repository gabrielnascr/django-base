from decouple import config
from .base import BASE_DIR


STATIC_URL = config('STATIC_URL', default='/static/')
MEDIA_URL = config('MEDIA_URL', default='/media/')

MEDIA_ROOT = BASE_DIR.child('public', 'media')
STATIC_ROOT = BASE_DIR.child('public', 'static')

STATICFILES_DIRS = [
    BASE_DIR.child('src', 'static'),
]
