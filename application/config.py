from kivy import Config

__all__ = ['load_config']


def load_config():
    Config.set(
        'kivy', 'keyboard_mode', 'systemanddock'
    )
