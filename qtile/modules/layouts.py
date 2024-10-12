from libqtile import layout
from libqtile.config import Match
from .widgets import *

layouts = [
    layout.Columns(
        margin=8,  # Adjust this for spacing
        border_focus=dracula["cyan"],
        border_normal=dracula["selection"],
        num_columns=3,  # Maximum of 3 columns
        split=True,  # Prioritize vertical splits
    ),
    layout.MonadTall(
        margin=8,
        border_focus=dracula["cyan"],
        border_normal=dracula["background"],
    ),
    # layout.MonadWide(
    #     margin=8,
    #     border_focus=dracula["cyan"],
    #     border_normal=dracula["background"]
    # ),
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
