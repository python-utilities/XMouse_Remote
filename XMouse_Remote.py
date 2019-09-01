#!/usr/bin/env python


if __name__ != '__main__':
    raise Exception("This file must be used as a command-line tool!")


import time
from argparse import ArgumentParser
from os.path import basename
from sys import argv

from lib.modules.xmouse_remote import XMouse_Remote


__script_name__ = basename(argv[0])


__usage__ = """
Some command options may be combined, for example to _drag_ button ID `1`...


  {script_name} --press-id 1 --delays 0.01 0.01 --move-relative 5 5 --release-id 1


Order of arguments parsed

0   --press-id or --press-name
1   --delays[0]
2   --move-absolute or --move-relative
3   --delays[1]
4   --click-id or --click-name
5   --release-id or --release-name
6   --location
""".format(script_name = __script_name__)

__epilog__ = """
"""


__license__ = """
Python2/3 mouse command-line wrapper API for `Xlib`
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


arg_parser = ArgumentParser(prog = basename(argv[0]),
                            usage = __usage__,
                            epilog = '%(prog)s source available at https://github.com/python-utilities/XMouse_Remote')

arg_parser.add_argument('--click-id',
                        help = 'Button ID number to click, eg. `1`',
                        type = int)

arg_parser.add_argument('--click-name',
                        help = 'Button name to click, eg. `button_left`',
                        type = str,
                        default = None)

arg_parser.add_argument('--click-times',
                        help = 'Number of times to click button ID or name',
                        type = int,
                        default = 1)

arg_parser.add_argument('--delays',
                        help = 'List of seconds to wait before and after movement',
                        type = float,
                        default = [0, 0],
                        nargs = '+')

arg_parser.add_argument('--display',
                        help = 'Display address, set if `DISPLAY` environment variable is **not** set; eg. `:0`')

arg_parser.add_argument('--location',
                        help = 'Prints current `x y` coordinates of mouse',
                        action = 'store_true',
                        default = False)

arg_parser.add_argument('--move-absolute',
                        help = 'Move mouse to absolute `x y` coordinates',
                        default = [],
                        type = int,
                        nargs = '+')

arg_parser.add_argument('--move-relative',
                        help = 'Move mouse relative `x y` distance from current location',
                        default = [],
                        type = int,
                        nargs = '+')

arg_parser.add_argument('--press-id',
                        help = 'Button ID number to press, eg. `1`',
                        type = int)

arg_parser.add_argument('--press-name',
                        help = 'Button name to press, eg. `button_left`',
                        type = str,
                        default = None)

arg_parser.add_argument('--release-id',
                        help = 'Button ID number to release, eg. `1`',
                        type = int)

arg_parser.add_argument('--release-name',
                        help = 'Button name to release, eg. `button_left`',
                        type = str,
                        default = None)

arg_parser.add_argument('--sync',
                        help = 'Wait for Xlib to think that things have synced',
                        action = 'store_true',
                        default = False)

parsed_arguments = {
    'click_id': arg_parser.parse_known_args()[0].click_id,
    'click_name': arg_parser.parse_known_args()[0].click_name,
    'click_times': arg_parser.parse_known_args()[0].click_times,
    'delays': arg_parser.parse_known_args()[0].delays,
    'display': arg_parser.parse_known_args()[0].display,
    'location': arg_parser.parse_known_args()[0].location,
    'move_absolute': arg_parser.parse_known_args()[0].move_absolute,
    'move_relative': arg_parser.parse_known_args()[0].move_relative,
    'press_id': arg_parser.parse_known_args()[0].press_id,
    'press_name': arg_parser.parse_known_args()[0].press_name,
    'release_id': arg_parser.parse_known_args()[0].release_id,
    'release_name': arg_parser.parse_known_args()[0].release_name,
    'sync': arg_parser.parse_known_args()[0].sync,
}


mouse = XMouse_Remote(display = parsed_arguments.get('display', None))

if parsed_arguments.get('press_id'):
    mouse.button_press(detail = parsed_arguments['press_id'], sync = parsed_arguments['sync'])
elif parsed_arguments.get('press_name'):
    mouse.button_press(button_name = parsed_arguments['press_name'], sync = parsed_arguments['sync'])


if parsed_arguments.get('delays', [0, 0])[0] > 0:
    time.sleep(parsed_arguments['delays'][0])

if parsed_arguments.get('move_absolute') != []:
    mouse.move_absolute(*parsed_arguments['move_absolute'], sync = parsed_arguments['sync'])
elif parsed_arguments.get('move_relative') != []:
    mouse.move_relative(*parsed_arguments['move_relative'], sync = parsed_arguments['sync'])

if parsed_arguments.get('delays', [0, 0])[1] > 0:
    time.sleep(parsed_arguments['delays'][1])


if parsed_arguments.get('click_id'):
    mouse.button_click(detail = parsed_arguments['click_id'],
                       times = parsed_arguments['click_times'],
                       sync = parsed_arguments['sync'])
elif parsed_arguments.get('click_name'):
    mouse.button_click(button_name = parsed_arguments['click_name'],
                       times = parsed_arguments['click_times'],
                       sync = parsed_arguments['sync'])


if parsed_arguments.get('release_id'):
    mouse.button_release(detail = parsed_arguments['release_id'], sync = parsed_arguments['sync'])
elif parsed_arguments.get('release_name'):
    mouse.button_release(button_name = parsed_arguments['release_name'], sync = parsed_arguments['sync'])


if parsed_arguments.get('location', False):
    print(" ".join(str(i) for i in mouse.location))
