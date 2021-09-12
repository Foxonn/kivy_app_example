from ...core.BaseLabel import BaseLabel

__all__ = ['SeventhLabel']


class SeventhLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "0"
        super().__init__(**kwargs)
