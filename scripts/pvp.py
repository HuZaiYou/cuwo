# Copyright (c) Mathias Kaerlev 2013-2014.
#
# This file is part of cuwo.
#
# cuwo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cuwo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cuwo.  If not, see <http://www.gnu.org/licenses/>.

"""
Player versus player mode!
"""

from cuwo.script import ServerScript, ConnectionScript
from cuwo.constants import HOSTILE_FLAG


class VersusConnection(ConnectionScript):
    def on_join(self, event):
        self.connection.entity.flags |= HOSTILE_FLAG

    def on_flags_update(self, event):
        self.connection.entity.flags |= HOSTILE_FLAG

    def on_kill(self, event):
        self.server.send_chat('%s killed %s!' % (self.connection.name,
                                                 event.target.name))


class VersusServer(ServerScript):
    connection_class = VersusConnection

    def get_mode(self, event):
        return 'pvp'


def get_class():
    return VersusServer
