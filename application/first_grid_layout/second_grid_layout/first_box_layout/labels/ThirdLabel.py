from ...core.BaseLabel import BaseLabel

__all__ = ['ThirdLabel']


class ThirdLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "Моносахара"
        super().__init__(**kwargs)
