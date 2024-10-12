#!/bin/sh
feh --bg-fill /home/nico/Pictures/wallpapers/pexels-le-anh-tuan-15613069.jpg
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
