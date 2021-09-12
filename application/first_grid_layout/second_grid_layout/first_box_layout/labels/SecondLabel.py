from ...core.BaseLabel import BaseLabel

__all__ = ['SecondLabel']


class SecondLabel(BaseLabel):
    def __init__(self, **kwargs):
        self.text = "Нитратная соль"
        super().__init__(**kwargs)
