from kivy.uix.boxlayout import BoxLayout

__all__ = ['FirstBoxLayout']


class FirstBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        self.orientation = "vertical"
        self.padding = [30, 0, 0, 0]
        super().__init__(**kwargs)
