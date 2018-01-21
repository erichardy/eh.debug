# -*- coding: utf-8 -*-

from zope.publisher.browser import BrowserView
from plone import api
import logging


logger = logging.getLogger('eh.debug: ')


objs = []
objs.append('news')
objs.append('events')
objs.append('Members')
objs.append('slider')
objs.append('portfolio')
objs.append('features')
objs.append('morefeatures')
objs.append('services')
objs.append('moreservices')


class ehMiscInit(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        for obj in objs:
            o = portal.get(obj)
            if o:
                logger.info(o.getId())
                try:
                    o.exclude_from_nav = True
                    o.reindexObject()
                except Exception:
                    logger.info('Cannot exclude from nav : ' + o.getId())
        portal.setLayout('listing_view')
        self.request.response.redirect(portal.absolute_url())
# http://localhost:8080/Plone/selectViewTemplate?templateId=listing_view&_authenticator=e4c1ad67a0b4df753d0209fe36c160e1ad7decaf
