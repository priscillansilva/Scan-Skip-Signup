from __future__ import unicode_literals

from django.db import models
from mongoengine import connect

connect(
    name='test',
    username='user',
    password='12345',
    host='mongodb://admin:qwerty@localhost/production'
)
# Create your models here.

