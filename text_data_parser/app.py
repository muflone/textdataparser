##
#     Project: Text Data Parser
# Description: View text data files with definitions.
#      Author: Fabio Castelli (Muflone) <muflone@vbsimple.net>
#   Copyright: 2015 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .ui_main import UIMain
from .constants import *
from .gtkbuilder_loader import GtkBuilderLoader


class Application(Gtk.Application):
    def __init__(self, settings, parser, definitions_file, data_file):
        """Create the application object"""
        super(self.__class__, self).__init__(application_id=APP_ID)
        self.settings = settings
        self.parser = parser
        self.definitions_file = definitions_file
        self.data_file = data_file
        self.connect("activate", self.activate)
        self.connect('startup', self.startup)

    def startup(self, application):
        """Configure the application during the startup"""
        self.ui = UIMain(self,
                         self.settings,
                         self.parser,
                         self.definitions_file,
                         self.data_file)
        # Add the about action to the app menu
        action = Gio.SimpleAction(name="about")
        action.connect("activate", self.on_app_about_activate)
        self.add_action(action)
        # Add the quit action to the app menu
        action = Gio.SimpleAction(name="quit")
        action.connect("activate", self.on_app_quit_activate)
        self.add_action(action)
        # Add the app menu
        builder_appmenu = GtkBuilderLoader(FILE_UI_APPMENU)
        self.set_app_menu(builder_appmenu.app_menu)

    def activate(self, application):
        """Execute the application"""
        self.ui.run()

    def on_app_about_activate(self, action, data):
        """Show the about dialog from the app menu"""
        self.ui.on_action_application_about_activate(action)

    def on_app_quit_activate(self, action, data):
        """Quit the application from the app menu"""
        self.ui.on_action_application_quit_activate(action)
