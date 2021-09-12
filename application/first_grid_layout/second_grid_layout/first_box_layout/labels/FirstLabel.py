from ...core.BaseLabel import BaseLabel

__all__ = ['FirstLabel']


class FirstLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "Соль"
        super().__init__(**kwargs)
