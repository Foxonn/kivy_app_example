from ...core.BaseLabel import BaseLabel

__all__ = ['SixthLabel']


class SixthLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "0"
        super().__init__(**kwargs)
