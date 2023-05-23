from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#00000000"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method = 'line',
                                this_screen_border = catppuccin["blue"],
                                this_current_screen_border = catppuccin["blue"],
                                active = catppuccin["white"],
                                inactive = catppuccin["green"],
                                background = catppuccin["mantle"]),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground = catppuccin["mauve"],
                       background ="#00000000"),
                widget.Prompt(),
                widget.Spacer(
                    length=3,
                    background="#00000000"
                    ),
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
                    foreground=catppuccin["white"],
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background=catppuccin["mantle"]),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=catppuccin["mantle"]
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=catppuccin["mantle"]
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=catppuccin["mantle"]
                       ),    
                widget.Clock(format='󰥔 %Y-%m-%d %a %I:%M:%S %p',
                             background=catppuccin["mantle"],
                             foreground=catppuccin["green"]),
                                                widget.TextBox(                                                
                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground = catppuccin["green"],
                       ),   
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=catppuccin["red"]),
            ],
            30,  # height in px
            background=catppuccin["mantle"]  # background color
        ), ),
]
