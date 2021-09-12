from typing import (
    Any,
    Mapping,
)

from kivy.uix.widget import Widget

from .FourthBoxLayout import FourthBoxLayout
from .buttons.FirstButton import FirstButton

__all__ = ['register_fourth_box_layout']


def register_fourth_box_layout(
    ioc: Mapping[str, Any],
    widget: Widget
) -> None:
    layout = FourthBoxLayout()
    button = FirstButton()

    layout.add_widget(
        widget=button
    )

    ioc[FirstButton] = button
    ioc[FourthBoxLayout] = layout

    widget.add_widget(
        widget=layout
    )
