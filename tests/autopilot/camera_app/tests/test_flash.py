# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Copyright 2012 Canonical
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.

"""Tests for the Camera App flash"""

from __future__ import absolute_import

from testtools.matchers import Equals, NotEquals
from autopilot.matchers import Eventually

from camera_app.tests import CameraAppTestCase

import time

class TestCameraFlash(CameraAppTestCase):
    """Tests the flash"""

    """ This is needed to wait for the application to start.
        In the testfarm, the application may take some time to show up."""
    def setUp(self):
        super(TestCameraFlash, self).setUp()
        self.assertThat(self.main_window.get_qml_view().visible, Eventually(Equals(True)))

    def tearDown(self):
        super(TestCameraFlash, self).tearDown()

    """Test that flash modes cycle properly"""
    def test_cycle_flash(self):
        flash_button = self.main_window.get_flash_button()

        #ensure initial state
        self.assertThat(flash_button.flashState, Equals("off"))
        self.assertThat(flash_button.torchMode, Equals(False))

        self.mouse.move_to_object(flash_button)

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("on")))
        self.assertThat(flash_button.torchMode, Equals(False))

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("auto")))
        self.assertThat(flash_button.torchMode, Equals(False))

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("off")))
        self.assertThat(flash_button.torchMode, Equals(False))

    """Test that torch modes cycles properly"""
    def test_cycle_torch(self):
        flash_button = self.main_window.get_flash_button()
        record_button = self.main_window.get_record_control()
        self.mouse.move_to_object(record_button)
        self.mouse.click()

        #ensure initial state
        self.assertThat(flash_button.flashState, Equals("off"))
        self.assertThat(flash_button.torchMode, Equals(True))

        self.mouse.move_to_object(flash_button)

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("on")))
        self.assertThat(flash_button.torchMode, Equals(True))

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("off")))
        self.assertThat(flash_button.torchMode, Equals(True))

    """When switching between video and picture the previous flash state
       should be preserved"""
    def test_remember_state(self):
        flash_button = self.main_window.get_flash_button()
        record_button = self.main_window.get_record_control()

        # Change flash mode, then switch to camera, then back to flash and verify
        # that previous state is preserved
        self.mouse.move_to_object(flash_button)
        self.mouse.click()
        self.mouse.click()
        old_flash_state = flash_button.flashState

        self.mouse.move_to_object(record_button)
        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("off")))
        self.assertThat(flash_button.torchMode, Equals(True))

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals(old_flash_state)))
        self.assertThat(flash_button.torchMode, Equals(False))

        # Now test the same thing in the opposite way, seeing if torch state is preserved
        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals("off")))
        self.assertThat(flash_button.torchMode, Equals(True))

        self.mouse.move_to_object(flash_button)
        self.mouse.click()
        old_torch_state = flash_button.flashState

        self.mouse.move_to_object(record_button)
        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals(old_flash_state)))
        self.assertThat(flash_button.torchMode, Equals(False))

        self.mouse.click()
        self.assertThat(flash_button.flashState, Eventually(Equals(old_torch_state)))
        self.assertThat(flash_button.torchMode, Equals(True))