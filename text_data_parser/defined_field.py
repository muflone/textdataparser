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


class DefinedField(object):
    def __init__(self, name, ftype, start, end, length, decimals, description):
        self.name = name
        self.type = ftype
        self.start = start
        self.end = end
        self.length = length
        self.decimals = decimals
        self.description = description

    def __repr__(self):
        return "<%s, name:'%s', description:'%s', type:%s, start:%d, end:%d, "
        "length:%d, decimals:%d>" % (
            self.__class__,
            self.name, self.description, self.type,
            self.start, self.end, self.length, self.decimals)
