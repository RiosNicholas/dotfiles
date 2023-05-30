from libqtile import bar, widget
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os
import subprocess

# DISPLAY SETTINGS
subprocess.call(["xrandr", "--output", "DP-0", "--mode", "1920x1080", "--rate", "144", "--primary"])
subprocess.call(["xrandr", "--output", "HDMI-0", "--mode", "1920x1080", "--left-of", "DP-0"])

# SCREENS
screens = [
    Screen(
        top=bar.Bar(
            [  
                widget.Spacer(
                    length=15,
                    background=catppuccin["mantle"],
                    ), 

                # LAUNCH ICON
                widget.Image(
                    filename='~/.config/qtile/assets/launch_Icon.png', 
                    margin=2, 
                    background=catppuccin["mantle"], 
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}
                    ),
                widget.Sep(
                    padding=4, 
                    linewidth=0, 
                    background=catppuccin["mantle"]
                    ), 
                
                # GROUPS
                widget.GroupBox(
                    fontweight="bold",
                    highlight_method = 'block',
                    this_screen_border = catppuccin["gray"],
                    this_current_screen_border = catppuccin["crust"],
                    block_highlight_text_color= catppuccin["white"],
                    active = catppuccin["crust"],
                    inactive = catppuccin["crust"],
                    background = catppuccin["mauve"],
                    urgent_alert_method="block",
                    urgent_border=catppuccin["lavender"],
                    urgent_text=catppuccin["crust"],
                    rounded=True,
                    disable_drag=True,
                    fontsize=13,
                    borderwidth=3,
                    corner_radius=12,  # Set the corner radius value as desired
                ),

                # CURRENT LAYOUT ICON
                widget.CurrentLayoutIcon(scale=0.6),
                widget.Spacer(
                    length=10,
                    background=catppuccin["mantle"],
                ),

                # PROMPT
                widget.Prompt(),
                widget.Spacer(length=10),

                # WINDOW NAME
                widget.WindowName(
                    foreground = catppuccin["sapphire"],
                    fmt='{}'
                    ),
                
                # VOLUME/MEDIA
                widget.Mpris2(
                    foreground=catppuccin["crust"],
                    background=catppuccin["yellow"],
                    objname='org.mpris.MediaPlayer2.spotify',
                    display_metadata=["xesam:title", "xesam:artist"],
                    paused_text="\uf001 (\uead1) {track} \uf001",
                    playing_text="\uf001 (\ueb2c) {track} \uf001",
                    scroll=True,
                    scroll_step=4,
                    scroll_interval=0.2,
                    scroll_clear=False,
                    scroll_delay=2,
                    width=200,
                    padding=10,
                    name="musicwidget",
                ),
                volume, 

                # MEMORY    
                widget.Memory(
                    background=catppuccin["maroon"],
                    foreground=catppuccin["crust"],
                    format=" {MemUsed:.0f}{mm}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                    padding=10,

                ),
                # CLOCK/DATE   
                widget.Clock(format=' %m-%d %a %I:%M:%S %p',
                    background=catppuccin["blue"],
                    foreground=catppuccin["crust"],
                    padding=10,
                    ),

                # POWER BUTTON
                widget.Spacer(
                    length=5,
                    background=catppuccin["mantle"],
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=catppuccin["red"]
                ),
                widget.Spacer(
                    length=15,
                    background=catppuccin["mantle"],
                ),
            ],
            30,  # height in px
            background=catppuccin["mantle"]  # background color
        ), 
    ),
]
