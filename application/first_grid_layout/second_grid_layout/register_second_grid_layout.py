from typing import (
    Any,
    Mapping,
)

from kivy.uix.widget import Widget

from .SecondGridLayout import SecondGridLayout
from .first_box_layout.register_first_box_layout import (
    register_first_box_layout
)
from .second_box_layout.register_second_box_layout import (
    register_second_box_layout
)

__all__ = ['register_second_grid_layout']


def register_second_grid_layout(
    ioc: Mapping[str, Any],
    widget: Widget
) -> None:
    grid = SecondGridLayout()
    register_first_box_layout(
        ioc=ioc,
        widget=grid
    )
    register_second_box_layout(
        ioc=ioc,
        widget=grid
    )
    widget.add_widget(
        widget=grid
    )
    ioc[SecondGridLayout] = grid
