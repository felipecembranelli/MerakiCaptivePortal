__author__ = 'feliperc'
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-15 -*-


#******************************************************************************
# Imports
#******************************************************************************

import logging
import webapp2
import json
#from google.appengine.ext.ndb import model
from webapp2_extras.appengine.auth.models import User
import datetime
from time import mktime
#******************************************************************************
# SocialPromo Handler
#******************************************************************************

# url sample http://atlantean-force-90113.appspot.com/rest/SocialPromoQueue?campaignId=C9

class captivePortalHandler(webapp2.RequestHandler):
  def get(self):
    logging.getLogger().setLevel(logging.DEBUG)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.headers['charset'] = 'utf-8'

    #try:

    logging.info('Get all users')

    userList = self.getAllUsers()

    logging.info('Finished')

    result = [c.to_dict() for c in userList.fetch()]

    logging.info(result)

    self.SendJson(result)

  def getAllUsers(self):
    return User.query()

    return users

  def SendJson(self, r):
    self.response.headers['content-type'] = 'text/plain'
    self.response.write(json.dumps(r, cls=customJsonEncoder))


class customJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)
