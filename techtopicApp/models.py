from django.db import models

# Create your models here.

# -*- encoding: utf-8 -*-
from mongoengine import *
from mongoengine.django.auth import User

class Topics(Document):
    # Topic title
    topic = StringField(required=True)
    # introduce
    introduce = StringField()
    # auther
    auther = ReferenceField(User)
    # create time
    createtime = DateTimeField()

class Comments(Document):
    # context
    context = StringField(required=True)
    # commtime
    commtime = DateTimeField()
    # topic
    topiclink = ReferenceField(Topics)
    # user
    auther = ReferenceField(User)



