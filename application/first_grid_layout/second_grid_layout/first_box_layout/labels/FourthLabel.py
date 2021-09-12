from ...core.BaseLabel import BaseLabel

__all__ = ['FourthLabel']


class FourthLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "Старты"
        super().__init__(**kwargs)
