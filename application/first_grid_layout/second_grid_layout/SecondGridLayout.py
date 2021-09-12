from kivy.uix.gridlayout import GridLayout

__all__ = ['SecondGridLayout']


class SecondGridLayout(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 2
        super().__init__(**kwargs)
