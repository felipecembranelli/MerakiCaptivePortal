# -*- coding: utf-8 -*-
# -*- coding: iso-8859-15 -*-

#******************************************************************************
# Imports
#******************************************************************************

import webapp2
from handlers.captivePortalHandler import *
from handlers.logHandler import *

#******************************************************************************
# Entry point
#******************************************************************************

app = webapp2.WSGIApplication([
    ('/api/captivePortalHandler', captivePortalHandler),
    ('/api/logHandler', logHandler)
    ],debug=True)
