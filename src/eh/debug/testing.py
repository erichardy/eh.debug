# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eh.debug


class EhDebugLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=eh.debug)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eh.debug:default')


EH_DEBUG_FIXTURE = EhDebugLayer()


EH_DEBUG_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EH_DEBUG_FIXTURE,),
    name='EhDebugLayer:IntegrationTesting'
)


EH_DEBUG_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EH_DEBUG_FIXTURE,),
    name='EhDebugLayer:FunctionalTesting'
)


EH_DEBUG_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EH_DEBUG_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EhDebugLayer:AcceptanceTesting'
)
