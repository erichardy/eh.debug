# -*- coding: utf-8 -*-

from zope.publisher.browser import BrowserView

import pdb


class debug(BrowserView):
    def __call__(self):
        # context = self.context
        pdb.set_trace()
