# A simple tictactoe activity for SugarLabs
# Copyright (C) 2020  Aditya Pratap Singh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity import activity


class TicTacToe(activity.Activity):

    def __init__(self, handle):
        self.tcount = 0
        self.track = set()
        activity.Activity.__init__(self, handle)

        self.max_participants = 1

        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        vbox = Gtk.VBox(spacing=20)

        self.set_canvas(vbox)
        vbox.show()

        self.turn = "X"
        self.prevturn = "X"
        self.turnview = Gtk.Label(label=self.turn+"'s turn")
        self.storex = {"dl": 0, "dr": 0, "v1": 0,
                       "v2": 0, "v3": 0, "h1": 0, "h2": 0, "h3": 0}
        self.storeo = {"dl": 0, "dr": 0, "v1": 0,
                       "v2": 0, "v3": 0, "h1": 0, "h2": 0, "h3": 0}
        self.list = [[], [], []]
        self.scorex = Gtk.Label(label="")
        self.scoreo = Gtk.Label(label="")
        self.x = self.o = 0

        self.scorex.set_markup("<span font='12'> X:   0 </span>")
        self.scoreo.set_markup("<span font='12'> O:   0 </span>")
        hbox = Gtk.Box(spacing=25)
        hbox.pack_start(self.scorex, True, True, 0)
        hbox.pack_start(Gtk.VSeparator(), 1, 1, 0)
        hbox.pack_start(self.scoreo, 1, 1, 0)
        label1 = Gtk.Label(label="")
        label1.set_markup("<span font='15'> LEADERBOARD </span>")
        vbox.pack_start(label1, True, True, 0)
        vbox.pack_start(hbox, 1, 1, 0)

        self.scorex.show()
        self.scoreo.show()
        self.turnview.show()
        hbox.show()
        label1.show()

        sep = Gtk.HSeparator()
        sep.show()
        vbox.pack_start(sep, True, True, 0)
        self.turnview.set_markup("<span font='25'>"+self.turn+"'s turn</span>")

        vbox.pack_start(self.turnview, True, True, 0)
        grid = Gtk.Grid()
        grid.show()
        vbox.pack_start(grid, True, True, 0)
        credits = Gtk.Label(label="")  # , xalign=1)
        credits.set_markup(
            """<span font='10'> Made with ❤ by <a href='https://www.github.com/devmrfitz'>
Aditya </a></span>""")
        credits.show()
        vbox.pack_start(credits, 1, 1, 0)
        credits.show()

        for _ in range(3):
            for __ in range(3):
                self.list[_].append(Gtk.Button())
                self.list[_][__].connect("clicked", self.click, _, __)

        grid.attach(self.list[0][0], 0, 0, 1, 1)

        grid.attach_next_to(
            self.list[0][1], self.list[0][0], Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(
            self.list[0][2], self.list[0][1], Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(
            self.list[1][0], self.list[0][0], Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(
            self.list[1][1], self.list[1][0], Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(
            self.list[1][2], self.list[1][1], Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(
            self.list[2][0], self.list[1][0], Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(
            self.list[2][1], self.list[2][0], Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(
            self.list[2][2], self.list[2][1], Gtk.PositionType.RIGHT, 1, 1)

        for li in self.list:
            for button in li:
                button.set_label("")
                button.show()
                button.get_child().set_markup("<span font='70'>     </span>")

    def click(self, widget, *uu):
        if widget in self.track:
            return 0
        self.track.add(widget)
        _ = int(uu[0])
        __ = int(uu[1])
        widget.get_child().set_markup("<span font='70'> "
                                      + self.turn+" </span>")
        if self.turn == "X":
            if _ == 0:
                if __ == 0:
                    self.storex["dl"] += 1
                    self.storex["v1"] += 1
                    self.storex["h1"] += 1
                elif __ == 1:
                    self.storex["v2"] += 1
                    self.storex["h1"] += 1
                elif __ == 2:
                    self.storex["v3"] += 1
                    self.storex["h1"] += 1
                    self.storex["dr"] += 1
            elif _ == 1:
                if __ == 0:
                    self.storex["v1"] += 1
                    self.storex["h2"] += 1
                elif __ == 1:
                    self.storex["v2"] += 1
                    self.storex["h2"] += 1
                    self.storex["dl"] += 1
                    self.storex["dr"] += 1
                elif __ == 2:
                    self.storex["v3"] += 1
                    self.storex["h2"] += 1
            elif _ == 2:
                if __ == 0:
                    self.storex["v1"] += 1
                    self.storex["h3"] += 1
                    self.storex["dr"] += 1
                elif __ == 1:
                    self.storex["v2"] += 1
                    self.storex["h3"] += 1
                elif __ == 2:
                    self.storex["v3"] += 1
                    self.storex["h3"] += 1
                    self.storex["dl"] += 1
            self.turn = "O"
        else:
            if _ == 0:
                if __ == 0:
                    self.storeo["dl"] += 1
                    self.storeo["v1"] += 1
                    self.storeo["h1"] += 1
                elif __ == 1:
                    self.storeo["v2"] += 1
                    self.storeo["h1"] += 1
                elif __ == 2:
                    self.storeo["v3"] += 1
                    self.storeo["h1"] += 1
                    self.storeo["dr"] += 1
            elif _ == 1:
                if __ == 0:
                    self.storeo["v1"] += 1
                    self.storeo["h2"] += 1
                elif __ == 1:
                    self.storeo["v2"] += 1
                    self.storeo["h2"] += 1
                    self.storeo["dl"] += 1
                    self.storeo["dr"] += 1
                elif __ == 2:
                    self.storeo["v3"] += 1
                    self.storeo["h2"] += 1
            elif _ == 2:
                if __ == 0:
                    self.storeo["v1"] += 1
                    self.storeo["h3"] += 1
                    self.storeo["dr"] += 1
                elif __ == 1:
                    self.storeo["v2"] += 1
                    self.storeo["h3"] += 1
                elif __ == 2:
                    self.storeo["v3"] += 1
                    self.storeo["h3"] += 1
                    self.storeo["dl"] += 1
            self.turn = "X"
        self.turnview.set_markup("<span font='25'>"+self.turn+"'s turn</span>")
        if 3 in self.storex.values():
            self.declare_winner("X")
        if 3 in self.storeo.values():
            self.declare_winner("O")
        if self.track.__len__() == 9:
            self.declare_winner()
            return 0

    def declare_winner(self, ch=None):
        if ch is None:
            if self.prevturn == "X":
                self.prevturn = "O"
                self.turn = "O"
            else:
                self.prevturn = "X"
                self.turn = "X"
            self.turnview.set_markup(
                "<span font='25'> It's a draw!!! " +
                self.turn+"'s turn </span>")
        else:
            self.incscore(ch)
            self.turn = ch.upper()
            self.turnview.set_markup(
                "<span font='25'>"+ch.upper()+" wins!!! " +
                self.turn+"'s turn</span>")

        for li in self.list:
            for button in li:
                button.set_label("")
                button.get_child().set_markup("<span font='70'>     </span>")
        self.storex = {"dl": 0, "dr": 0, "v1": 0,
                       "v2": 0, "v3": 0, "h1": 0, "h2": 0, "h3": 0}
        self.storeo = {"dl": 0, "dr": 0, "v1": 0,
                       "v2": 0, "v3": 0, "h1": 0, "h2": 0, "h3": 0}
        self.track = set()

    def incscore(self, ch):
        if ch.upper() == "X":
            self.x += 1
            self.scorex.set_markup(
                "<span font='12'> X:   "+str(self.x)+"</span>")
        elif ch.upper() == "O":
            self.o += 1
            self.scoreo.set_markup(
                "<span font='12'> O:   "+str(self.o)+"</span>")
