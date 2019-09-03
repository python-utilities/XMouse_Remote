# XMouse Remote
[heading__title]:
  #xmouse-remote
  "&#x2B06; Top of ReadMe File"


Python2/3 mouse wrapper API of `Xlib`


## [![Open Issues][badge__issues__xmouse_remote]][issues__xmouse_remote] [![Open Pull Requests][badge__pull_requests__xmouse_remote]][pull_requests__xmouse_remote] [![Latest commits][badge__commits__xmouse_remote__gh_pages]][commits__xmouse_remote__gh_pages]



------


#### Table of Contents


- [:arrow_up: Top of ReadMe File][heading__title]

- [:zap: Quick Start][heading__quick_start]

  - [:floppy_disk: Download][heading__install]
  - [:arrow_up: Update][heading__update]
  - [:shell: Utilize XMouse Remote][heading__utilize]

- [&#x1F5D2; Notes][heading__notes]

- [&#x2696; License][heading__license]


------



## Quick Start
[heading__quick_start]:
  #quick-start
  "&#x1F41A; Perhaps as easy as one, 2.0,..."


### Install
[heading__install]:
  #install
  "&#x1F4BE; It may be just this easy..."


```Bash
mkdir ~/git/hub

cd ~/git/hub
```


**Git Clone**


```Bash
git clone --recurse-submodules\
 --single-branch\
 --branch gh-pages\
 git@github.com:python-utilities/XMouse_Remote.git
```


**Install Python requirements**


```Bash
pip3 install -r requirements.txt --user
```


**Symbolically link**


```Bash
mkdir -vp ~/bin

ln -s "${HOME}/git/hub/XMouse_Remote/XMouse_Remote.py" "${HOME}/bin/XMouse_Remote"
```


### Update
[heading__update]:
  #update
  "&#x2B06; Updating source and dependencies tips"


```Bash
cd "${HOME}/git/hub/XMouse_Remote"

git pull

git submodule update --init --merge --recursive

pip3 install -r requirements.txt --user
```


### Utilize XMouse Remote
[heading__utilize]:
  #utilize-xmouse-remote
  "&#x1F41A; How to make use of this branch"


**On the command-line**


```Bash
XMouse_Remote --location

XMouse_Remote --press-id 1 --delays 0.01 0.01 --move-relative 5 5 --release-id 1

XMouse_Remote --location
```


**Within a script**


```Bash
#!/usr/bin/env bash


mouse_location(){ printf '%s\n' "$(XMouse_Remote --location)"; }

mouse_relative_drag(){
  _id="${1:-1}"
  _x="${2:-0}"
  _y="${3:-0}"
  XMouse_Remote --press-id "${_id:?}"\
   --move-relative "${_x}" "${_y}"
   --delays 0.01 0.01
   --release-id "${_id}"
}


mouse_relative_drag "1" "5" "5"
```


**Or as a keyboard remapping `~/.config/openbox/lxde-pi-rc.xml`**


```XML
<?xml version="1.0"?>
<openbox config>
  <theme>
    <font place="ActiveWindow">
      <name>PibotoLt</name>
      <size>18</size>
      <weight>Normal</weight>
      <slant>Normal</slant>
    </font>

    <font place="ActiveWindow">
      <name>PibotoLt</name>
      <size>18</size>
      <weight>Normal</weight>
      <slant>Normal</slant>
    </font>

    <invHandleWidth>20</invHandleWidth>
    <titleColor>#4d98f5</titleColor>
    <textColor>#ffffff</textColor>
  </theme>


  <!--
    Above theme is from Raspberry Pi, other systems may appear different

    Bellow maps number pad to XMouse_Remote actions based off "Num Lock" state
  -->

  <!-- Move cursor left and up -->
  <keybind key="KP_7">
    <action name="Execute">
      <command>XMouse_Remote --move-relative -5 -5</command>
    </action>
  </keybind>

  <!-- Move cursor up -->
  <keybind key="KP_Up">
    <action name="Execute">
      <command>XMouse_Remote --move-relative 0 -5</command>
    </action>
  </keybind>

  <!-- Move cursor right and up -->
  <keybind key="KP_9">
    <action name="Execute">
      <command>XMouse_Remote --move-relative 5 -5</command>
    </action>
  </keybind>

  <!-- Move cursor right -->
  <keybind key="KP_Right">
    <action name="Execute">
      <command>XMouse_Remote --move-relative -5 0</command>
    </action>
  </keybind>

  <!-- Move cursor right and down -->
  <keybind key="KP_3">
    <action name="Execute">
      <command>XMouse_Remote --move-relative 5 5</command>
    </action>
  </keybind>

  <!-- Move cursor down -->
  <keybind key="KP_Down">
    <action name="Execute">
      <command>XMouse_Remote --move-relative 0 5</command>
    </action>
  </keybind>

  <!-- Move cursor left and down -->
  <keybind key="KP_1">
    <action name="Execute">
      <command>XMouse_Remote --move-relative -5 5</command>
    </action>
  </keybind>

  <!-- Move cursor left -->
  <keybind key="KP_Left">
    <action name="Execute">
      <command>XMouse_Remote --move-relative -5 0</command>
    </action>
  </keybind>

  <keybind key="KP_Begin">
    <action name="Execute">
      <command>
        XMouse_Remote --move-absolute $(XMouse_Remote --screen-size awk '{print $1 / 2, $2 / 2}')
      </command>
    </action>
  </keybind>

  <!-- Left click on 0 when "Num Lock" is off -->
  <keybind key="KP_Insert">
    <action name="Execute">
      <command>XMouse_Remote --click-id 1</command>
    </action>
  </keybind>

  <!-- Right click on enter -->
  <keybind key="KP_Enter">
    <action name="Execute">
      <command>XMouse_Remote --click-id 2</command>
    </action>
  </keybind>

  <!-- Middle click on decimal point -->
  <keybind key="KP_Delete">
    <action name="Execute">
      <command>XMouse_Remote --click-id 3</command>
    </action>
  </keybind>

  <!-- Scroll left and right on 4 and 6 -->
  <keybind key="4">
    <action name="Execute">
      <command>XMouse_Remote --scroll-x 3</command>
    </action>
  </keybind>

  <keybind key="6">
    <action name="Execute">
      <command>XMouse_Remote --scroll-x -3</command>
    </action>
  </keybind>

  <!-- Scroll up and down on 8 and 2 -->
  <keybind key="8">
    <action name="Execute">
      <command>XMouse_Remote --scroll-y 3</command>
    </action>
  </keybind>

  <keybind key="2">
    <action name="Execute">
      <command>XMouse_Remote --scroll-y -3</command>
    </action>
  </keybind>

</openbox>
```


> Issue `openbox --reconfigure` to reload configurations or reboot the device for changes to take effect.


**:tada: Excellent :tada:** your project is now ready to begin unitizing code from this repository!


___


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional resources and things to keep in mind when developing"


There maybe bugs or missing features, Pull Requests are welcome.

___


## License
[heading__license]:
  #license
  "&#x2696; Legal bits of Open Source software"


Legal bits of Open Source software


```
XMouse Remote ReadMe documenting how things like this could be utilized
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
```



[badge__commits__xmouse_remote__gh_pages]:
  https://img.shields.io/github/last-commit/python-utilities/xmouse_remote/gh-pages.svg

[commits__xmouse_remote__gh_pages]:
  https://github.com/python-utilities/xmouse_remote/commits/gh-pages
  "&#x1F4DD; History of changes on this branch"


[xmouse_remote__community]:
  https://github.com/python-utilities/xmouse_remote/community
  "&#x1F331; Dedicated to functioning code"


[xmouse_remote__gh_pages]:
  https://github.com/python-utilities/xmouse_remote/tree/gh-pages
  "Source code examples hosted thanks to GitHub Pages!"


[badge__issues__xmouse_remote]:
  https://img.shields.io/github/issues/python-utilities/xmouse_remote.svg

[issues__xmouse_remote]:
  https://github.com/python-utilities/xmouse_remote/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."


[badge__pull_requests__xmouse_remote]:
  https://img.shields.io/github/issues-pr/python-utilities/xmouse_remote.svg

[pull_requests__xmouse_remote]:
  https://github.com/python-utilities/xmouse_remote/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"
