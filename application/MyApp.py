from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager

__all__ = ['MyApp']


class Container(GridLayout):
    def __init__(self, **kwargs):
        self.rows = 3
        super().__init__(**kwargs)


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.container: Container = Container()
        super().__init__(**kwargs)

    def build(self):
        self.title = "CoppaApp"
        them_manager = ThemeManager()
        them_manager.theme_style = 'Light'
        return self.container
