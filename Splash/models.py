__author__ = 'feliperc'

from google.appengine.ext import ndb


class CustomUserInfo(ndb.Model):
    userName = ndb.StringProperty()