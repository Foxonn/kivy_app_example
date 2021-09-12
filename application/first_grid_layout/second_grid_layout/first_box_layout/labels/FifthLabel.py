from ...core.BaseLabel import BaseLabel

__all__ = ['FifthLabel']


class FifthLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "Время засолки"
        super().__init__(**kwargs)
