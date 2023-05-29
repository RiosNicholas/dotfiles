from libqtile import bar
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
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["mauve"],
                ),
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
                ),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["mauve"]
                ), 

                widget.Spacer(
                    length=10,
                    background=catppuccin["mantle"],
                ),
                widget.Prompt(),
                widget.Spacer(length=10),
                widget.WindowName(
                    foreground = catppuccin["sapphire"], \
                    fmt='{}'
                    ),
                           
                widget.CurrentLayoutIcon(scale=0.75),

                widget.Systray(
                    background=catppuccin["mantle"],
                    fontsize=2,
                ), 
                
                # VOLUME/MEDIA
                volume,  
                
                # MEMORY 
        
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground=catppuccin["flamingo"]
                ),   
                widget.Memory(
                    background=catppuccin["flamingo"],
                    foreground=catppuccin["crust"],
                    format="󰈀 {MemUsed:.0f}{mm}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["flamingo"],
                ),

                # CLOCK/DATE
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground=catppuccin["blue"]
                ),    
                widget.Clock(format=' %m-%d-%Y %a %I:%M:%S %p',
                    background=catppuccin["blue"],
                    foreground=catppuccin["crust"]),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["blue"],
                ),

                # POWER BUTTON
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
