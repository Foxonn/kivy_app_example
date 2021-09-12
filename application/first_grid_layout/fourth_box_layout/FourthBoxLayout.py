from kivy.uix.boxlayout import BoxLayout

__all__ = ['FourthBoxLayout']


class FourthBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.9, .15)
        self.padding = (30, 0, 30, 20)
