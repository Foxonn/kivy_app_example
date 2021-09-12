from kivy.uix.boxlayout import BoxLayout

__all__ = ['SecondBoxLayout']


class SecondBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        self.orientation = "vertical"
        self.size_hint = (0.5, 1)
        super().__init__(**kwargs)
