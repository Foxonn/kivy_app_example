from kivymd.uix.textfield.textfield import MDTextField

__all__ = ['FirstInput']


class FirstInput(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.font_size = "45sp"
        self.input_type = 'number'
        self.input_filter = 'int'
        self.hint_text = "Масса в граммах"
