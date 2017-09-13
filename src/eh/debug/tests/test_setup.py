# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from eh.debug.testing import EH_DEBUG_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that eh.debug is properly installed."""

    layer = EH_DEBUG_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eh.debug is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'eh.debug'))

    def test_browserlayer(self):
        """Test that IEhDebugLayer is registered."""
        from eh.debug.interfaces import (
            IEhDebugLayer)
        from plone.browserlayer import utils
        self.assertIn(IEhDebugLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EH_DEBUG_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['eh.debug'])

    def test_product_uninstalled(self):
        """Test if eh.debug is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'eh.debug'))

    def test_browserlayer_removed(self):
        """Test that IEhDebugLayer is removed."""
        from eh.debug.interfaces import \
            IEhDebugLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEhDebugLayer, utils.registered_layers())
