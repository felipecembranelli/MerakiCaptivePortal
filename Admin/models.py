__author__ = 'feliperc'

from google.appengine.ext import ndb


class TwitterUser(ndb.Model):
    userId = ndb.StringProperty()
    userName = ndb.StringProperty()
    userLocation = ndb.StringProperty()
    followersCount = ndb.StringProperty(indexed=False)


