from typing import (
    Any,
    Mapping,
)

from kivy.uix.widget import Widget

from .FirstAnchorLayout import FirstAnchorLayout
from .inputs.FirstInput import FirstInput

__all__ = ['register_first_anchor_layout']


def register_first_anchor_layout(
    ioc: Mapping[str, Any],
    widget: Widget,
) -> None:
    layout = FirstAnchorLayout()
    input = FirstInput()

    layout.add_widget(
        widget=input
    )

    ioc[FirstInput] = input
    ioc[FirstAnchorLayout] = layout

    widget.add_widget(
        widget=layout
    )
