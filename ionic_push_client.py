'''
Created on 02/07/2016

@author: Ismail Faizi
'''

import logging

from google.appengine.api import urlfetch


class IonicPushClient(object):
    """
    A simple client for sending push notification using Ionic Push Service

    @author: Ismail Faizi <kanafghan@gmail.com>
    """

    PUSH_API_URL = 'https://api.ionic.io/push/notifications'
    PUSH_API_TOKEN = '<put-your-app-api-token-here>'
    PUSH_PROFILE = '<put-your-profile-tag-here>'

    @classmethod
    def push(cls, tokens, alert, url=None, api_token=None):
        if 0 == len(alert):
            alert = "There are updates to check! :-D"

        if not url:
            url = cls.PUSH_API_URL

        if not api_token:
            api_token = cls.PUSH_API_TOKEN

        body = json.dumps({
            "tokens": tokens,
            "profile": cls.PUSH_PROFILE,
            "notification": {
                "message": alert
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % api_token
        }

        result = None
        try:
            result = urlfetch.fetch(url=url,
                                    payload=body,
                                    method=urlfetch.POST,
                                    follow_redirects=True,
                                    headers=headers)
            logging.info('Successfully sent the push notification "%s" with result %s.' % (alert, str(result)))
        except Exception, e:
            logging.error('There was an error sending push notification! Error: %s' % str(e))

        return result
