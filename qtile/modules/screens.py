from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#00000000"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background=catppuccin["mantle"], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background=catppuccin["mantle"]), 
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["mauve"],
                        ),
                widget.GroupBox(
                    highlight_method = 'block',
                    this_screen_border = catppuccin["gray"],
                    this_current_screen_border = catppuccin["mantle"],
                    active = catppuccin["sky"],
                    inactive = catppuccin["crust"],
                    background = catppuccin["mauve"]
                    ),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["mauve"]
                    ),
                widget.Prompt(),
                widget.WindowName(foreground = catppuccin["sapphire"], fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground=catppuccin["pink"],
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background=catppuccin["mantle"]),
                widget.Systray(icon_size = 20), 
                volume,  
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground=catppuccin["blue"]
                    ),    
                widget.Clock(format='󰥔 %Y-%m-%d %a %I:%M:%S %p',
                    background=catppuccin["blue"],
                    foreground=catppuccin["crust"]),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground = catppuccin["blue"],
                    ),

                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=catppuccin["red"]),
                 widget.Spacer(
                    length=5,
                    background=catppuccin["mantle"]
                    ),
            ],
            30,  # height in px
            background=catppuccin["mantle"]  # background color
        ), ),
]
