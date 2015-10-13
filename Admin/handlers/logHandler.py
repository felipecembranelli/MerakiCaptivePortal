__author__ = 'feliperc'
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-15 -*-

#******************************************************************************
# Imports
#******************************************************************************

import base64
import datetime
import logging
import time
import urllib
import webapp2
from google.appengine.api.logservice import logservice

# This sample gets the app request logs up to the current time, displays 5 logs
# at a time, including all AppLogs, with a Next link to let the user "page"
# through the results, using the RequestLog offset property.

#******************************************************************************
# Log Handler
#******************************************************************************

class logHandler(webapp2.RequestHandler):

    def get(self):
        logging.info('Starting Main handler')
        # Get the incoming offset param from the Next link to advance through
        # the logs. (The first time the page is loaded, there won't be any offset.)
        try:
            offset = self.request.get('offset') or None
            if offset:
                offset = base64.urlsafe_b64decode(str(offset))
        except TypeError:
            offset = None

        # Set up end time for our query.
        end_time = time.time()

        # Count specifies the max number of RequestLogs shown at one time.
        # Use a boolean to initially turn off visiblity of the "Next" link.
        count = 5
        show_next = False
        last_offset = None

        # Iterate through all the RequestLog objects, displaying some fields and
        # iterate through all AppLogs beloging to each RequestLog count times.
        # In each iteration, save the offset to last_offset; the last one when
        # count is reached will be used for the link.
        i = 0
        for req_log in logservice.fetch(end_time=end_time, offset=offset,
                                        minimum_log_level=logservice.LOG_LEVEL_INFO,
                                        include_app_logs=True):
            self.response.out.write('<br /> REQUEST LOG <br />')
            self.response.out.write(
                'IP: %s <br /> Method: %s <br /> Resource: %s <br />' %
                (req_log.ip, req_log.method, req_log.resource))
            self.response.out.write(
                'Date: %s<br />' %
                #datetime.datetime.fromtimestamp(req_log.end_time).strftime('%D %T UTC'))
                str(req_log.end_time))

            last_offset= req_log.offset
            i += 1

            for app_log in req_log.app_logs:
                self.response.out.write('<br />APP LOG<br />')
                self.response.out.write(
                    'Date: %s<br />' %
                    #datetime.datetime.fromtimestamp(app_log.time).strftime('%D %T UTC'))
                    str(req_log.end_time))
                self.response.out.write('<br />Message: %s<br />' % app_log.message)

            if i >= count:
                show_next = True
                break

        # Prepare the offset URL parameters, if any.
        if show_next:
            query = self.request.GET
            query['offset'] = base64.urlsafe_b64encode(last_offset)
            next_link = urllib.urlencode(query)
            self.response.out.write('<a href="/rest/logHandler?%s">Next</a>' % next_link)