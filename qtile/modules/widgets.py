from libqtile import widget
from libqtile import qtile

# catppuccin = {
#     "flamingo": "#f0c6c6",
#     "mauve": "#c6a0f6",
#     "pink": "#f5bde6",
#     "maroon": "#ee99a0",
#     "red": "#ed8796",
#     "peach": "#f5a97f",
#     "yellow": "#eed49f",
#     "green": "#a6da95",
#     "teal": "#8bd5ca",
#     "sapphire": "#7dc4e4",
#     "blue": "#8aadf4",
#     "sky": "#91d7e3",
#     "white": "#cad3f5",
#     "gray": "#6e738d",
#     "mantle": "#1e2030",
#     "crust": "#181926",
#     "lavender": "#b7bdf8",
#     "yellow": "#eed49f",
# }

dracula = {
    "background": "#282a36",
    "current_line": "#44475a",
    "selection": "#44475a",
    "foreground": "#f8f8f2",
    "comment": "#6272a4",
    "cyan": "#8be9fd",
    "green": "#50fa7b",
    "orange": "#ffb86c",
    "pink": "#ff79c6",
    "purple": "#bd93f9",
    "red": "#ff5555",
    "yellow": "#f1fa8c",
}


widget_defaults = dict(
    font='JetBrains Mono Nerd Font',
    fontsize=12,
    padding=10
)
extension_defaults = widget_defaults.copy()

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '󰝟'
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '󰝟'
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize=18,
    font='JetBrains Mono Nerd Font',
    padding=10,
    foreground=dracula["foreground"],
    background=dracula["cyan"],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
