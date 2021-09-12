from kivymd.uix.label import MDLabel

__all__ = ['BaseLabel']


class BaseLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = "25px"
        self.halign = "left"
        self.valign = "middle"
        self.text_size = (200, None)
