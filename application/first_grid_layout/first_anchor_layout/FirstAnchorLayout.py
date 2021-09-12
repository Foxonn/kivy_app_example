from kivy.uix.anchorlayout import AnchorLayout

__all__ = ['FirstAnchorLayout']


class FirstAnchorLayout(AnchorLayout):
    def __init__(self, **kwargs):
        self.size_hint = (1, 0.2)
        self.anchor_y = "top"
        self.padding = 30
        super().__init__(**kwargs)
