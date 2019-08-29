#!/usr/bin/env python3


from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input


__license__ = """
Python2/3 mouse wrapper API of `Xlib`
Copyright (C) 2019  S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class XMouse_Remote(object):
    """
    Python2/3 mouse wrapper API of `Xlib`

        mouse = XMouse_Remote(display = ':0')

        print("XMouse_Remote location -> {}".format(mouse.location))
        mouse.move_absolute(x = 5, y = 5)

    Note for script writers, most of the logics are in the following methods

    - button_press
    - button_release
    - move_absolute
    - scroll
    """

    def __init__(self, display = None, button_ids = None):
        """
        See -- http://python-xlib.sourceforge.net/doc/html/python-xlib_16.html#SEC15
        """
        self.display = Display(display)

        self.button_ids = button_ids
        if self.button_ids is None:
            self.button_ids = {
                'button_left': 1,
                'button_middle': 2,
                'button_right': 3,
                'scroll_up': 4,
                'scroll_down': 5,
                'scroll_left': 6,
                'scroll_right': 7
            }

        ## Used to prevent overwriting variables outside of class
        self._screen_width = self.display.screen().width_in_pixels
        self._screen_height = self.display.screen().height_in_pixels
        self._new_location = self.location
        self._target_id = 1
        self._x = self._new_location[0]
        self._y = self._new_location[1]
        self._coordinates = None

    @property
    def location(self):
        """
        Returns `[x, y]` list of coordinates that mouse cursor occupies
        """
        self._coordinates = self.display.screen().root.query_pointer()._data
        return [self._coordinates.get('root_x'), self._coordinates.get('root_y')]

    def button_click(self, x, y, detail = 1, button_name = None, times = 1, sync = True):
        """
        Calls `self.button_press(...)` and `self.button_release(...)` before returning `self.location`
        """
        for _ in range(times):
            self.button_press(x = x, y = y, detail = detail, button_name = button_name, sync = sync)
            self.button_release(x = x, y = y, detail = detail, button_name = button_name, sync = sync)

        return self.location

    def drag_absolute(self, x, y, detail = 1, button_name = None, sync = True):
        """
        Starting from `self.location`, moves to absolute coordinates while pressing defined button IDs
        """
        self.button_press(*self.location, detail = detail, button_name = button_name, sync = False)
        self.move_absolute(x = x, y = y, sync = False)
        self.button_release(x = x, y = y, detail = detail, button_name = button_name, sync = False)

        if sync:
            self.display.sync()

        return self.location

    def drag_relative(self, x, y, detail = 1, button_name = None, sync = True):
        """
        Starting from `self.location`, moves to relative coordinates while pressing defined button IDs
        """
        self.button_press(*self.location, detail = detail, button_name = button_name, sync = False)
        self.move_relative(x = x, y = y, sync = False)
        self.button_release(x = x, y = y, detail = detail, button_name = button_name, sync = False)

        if sync:
            self.display.sync()

        return self.location

    def button_press(self, x, y, detail = 1, button_name = None, sync = True):
        """
        Returns `self.location` after telaporting and pressing button ID or name
        """
        self.move_absolute(x = x, y = y, sync = sync)

        self._target_id = detail
        if button_name is not None:
            self._target_id = self.button_ids.get(button_name, 1)

        fake_input(self.display, event_type = X.ButtonPress, detail = self._target_id)

        if sync:
            self.display.sync()

        return self.location

    def button_release(self, x, y, detail = 1, button_name = None, sync = True):
        """
        Returns `self.location` after telaporting and releasing button ID or name
        """
        self.move_absolute(x = x, y = y, sync = sync)

        self._target_id = detail
        if button_name is not None:
            self._target_id = self.button_ids.get(button_name, 1)

        fake_input(self.display, event_type = X.ButtonRelease, detail = detail)

        if sync:
            self.display.sync()

        return self.location

    def move_absolute(self, x, y, sync = True):
        """
        Returns `self.location` after telaporting mouse if nessisary

        See -- https://github.com/python-xlib/python-xlib/blob/master/Xlib/ext/xtest.py
        """
        if (x, y) != self.location:
            fake_input(self.display, event_type = X.MotionNotify, x = x, y = y)

        if sync:
            self.display.sync()

        return self.location

    def move_relative(self, x = 0, y = 0, sync = True):
        """
        Returns `self.location` after moving relative distance from last coordinates
        """
        self._new_location = self.location

        if x != 0:
            self._new_location[0] = self._new_location[0] + x

        if y != 0:
            self._new_location[1] = self._new_location[1] + y

        return self.move_absolute(*self._new_location, sync = sync)

    def scroll(self, x = 0, y = 0):
        """
        Scroll up or left if positive and down or right if negative
        """
        if y > 0:
            self.button_click(*self.location, detail = self.button_ids.get('scroll_up', 4), times = y)
        elif y < 0:
            self.button_click(*self.location, detail = self.button_ids.get('scroll_down', 5), times = abs(y))

        if x > 0:
            self.button_click(*self.location, detail = self.button_ids.get('scroll_left', 6), times = x)
        elif x < 0:
            self.button_click(*self.location, detail = self.button_ids.get('scroll_right', 7), times = abs(x))
