#!/usr/bin/env python2
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

from text_data_parser import Application
from text_data_parser.parsers import DataParserFixed
from text_data_parser.settings import Settings

if __name__ == '__main__':
    parser = DataParserFixed()
    arg_definitions_file = None
    arg_data_file = None
    # Load the settings from the configuration file
    settings = Settings()
    # Start the application
    app = Application(
        settings=settings,
        parser=parser,
        definitions_file=arg_definitions_file,
        data_file=arg_data_file)
    app.run(None)
