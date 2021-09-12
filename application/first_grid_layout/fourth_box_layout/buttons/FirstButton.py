from kivymd.uix.button.button import MDRaisedButton

__all__ = ['FirstButton']


class FirstButton(MDRaisedButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Go!"
        self.size_hint = (1, 0.9)
