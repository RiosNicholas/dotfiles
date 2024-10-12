from libqtile import bar, widget
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os
import subprocess

# DISPLAY SETTINGS
#subprocess.call(["xrandr", "--output", "DP-0", "--mode", "1920x1080", "--rate", "144", "--primary", "--pos", "1080x420"])
#subprocess.call(["xrandr", "--output", "HDMI-0", "--mode", "1080x1920", "--left-of", "DP-0"])
subprocess.call(["xrandr", "--output", "DP-0", "--mode", "3440x1440", "--rate", "159.96"])


# SCREENS

screens = [
    Screen(
        top=bar.Bar(
            [  
                widget.Spacer(
                    length=15,
                    background=dracula["background"],
                ), 

                # LAUNCH ICON
                widget.Image(
                    filename='~/.config/qtile/assets/launch_Icon.png', 
                    margin=2, 
                    background=dracula["background"],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}
                    ),
                widget.Sep(
                    padding=4, 
                    linewidth=0, 
                    background=dracula["background"],
                ),
                
                # GROUPS
                widget.GroupBox(
                    fontweight="bold",
                    highlight_method='block',
                    this_screen_border=dracula["current_line"],
                    this_current_screen_border=dracula["selection"],
                    block_highlight_text_color=dracula["foreground"],
                    active=dracula["background"],
                    inactive=dracula["background"],
                    background=dracula["purple"],
                    urgent_alert_method="block",
                    urgent_border=dracula["orange"],
                    urgent_text=dracula["background"],
                    rounded=True,
                    disable_drag=True,
                    fontsize=13,
                    borderwidth=3,
                    corner_radius=12,
                ),

                # CURRENT LAYOUT ICON
                widget.CurrentLayoutIcon(scale=0.6),
                widget.Spacer(
                    length=10,
                    background=dracula["background"],
                ),

                # PROMPT
                widget.Prompt(),
                widget.Spacer(length=10),

                # WINDOW NAME
                widget.WindowName(
                    foreground=dracula["cyan"],
                    fmt='{}'
                ),
                
                # VOLUME/MEDIA
                widget.Mpris2(
                    foreground=dracula["background"],
                    background=dracula["green"],
                    objname='org.mpris.MediaPlayer2.spotify',  # This is the DBus identifier for Spotify
                    display_metadata=["xesam:title", "xesam:artist"],  # Metadata fields to display
                    paused_text="\uf001 (Paused) {track} \uf001",  # Text to display when paused
                    playing_text="\uf001 (Playing) {track} \uf001",  # Text to display when playing
                    scroll=True,  # Enable scrolling
                    scroll_step=1,  # Scrolling step size in pixels
                    scroll_interval=0.2,  # Time between scrolling steps (seconds)
                    scroll_clear=False,  # Do not clear the text when finished scrolling
                    scroll_delay=2,  # Delay before scrolling begins (seconds)
                    width=200,  # Widget width
                    padding=10,  # Padding around the widget
                    name="musicwidget",  # Optional name for the widget
                ),
                volume,  # Your custom volume widget instance


                # MEMORY    
                widget.Memory(
                    background=dracula["yellow"],
                    foreground=dracula["background"],
                    format=" {MemUsed:.0f}{mm}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                    padding=10,
                ),
                # CLOCK/DATE   
                widget.Clock(format=' %m-%d %a %I:%M:%S %p',
                    background=dracula["purple"],
                    foreground=dracula["background"],
                    padding=10,
                ),

                # POWER BUTTON
                widget.Spacer(
                    length=5,
                    background=dracula["background"],
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=dracula["red"]
                ),
                widget.Spacer(
                    length=15,
                    background=dracula["background"],
                ),
            ],
            # HEIGHT IN PX
            30,  
            
            # BACKGROUND COLOR
            background=dracula["background"]
        ), 
    ),
]
