from libqtile import widget
from libqtile import qtile

catppuccin = {
    "flamingo": "#f0c6c6",
    "mauve": "#c6a0f6",
    "pink": "#f5bde6",
    "maroon": "#ee99a0",
    "red": "#ed8796",
    "peach": "#f5a97f",
    "yellow": "#eed49f",
    "green": "#a6da95",
    "teal": "#8bd5ca",
    "sapphire": "#7dc4e4",
    "blue": "#8aadf4",
    "sky": "#91d7e3",
    "white": "#cad3f5",
    "gray": "#6e738d",
    "mantle": "#1e2030",
    "crust": "#181926",
    "lavender": "#b7bdf8",
}

widget_defaults = dict(
    font='JetBrains Mono Nerd Font',
    fontsize=12,
    padding=3
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
    foreground=catppuccin["green"],
    background=catppuccin["mantle"],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
