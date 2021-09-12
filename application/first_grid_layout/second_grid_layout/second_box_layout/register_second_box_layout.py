from typing import (
    Any,
    Mapping,
)

from kivy.uix.widget import Widget

from .SecondBoxLayout import SecondBoxLayout
from .labels.SixthLabel import SixthLabel
from .labels.SeventhLabel import SeventhLabel
from .labels.EighthLabel import EighthLabel
from .labels.NinthLabel import NinthLabel
from .labels.TenthLabel import TenthLabel

__all__ = ['register_second_box_layout']


def register_second_box_layout(
    ioc: Mapping[str, Any],
    widget: Widget,
) -> None:
    box = SecondBoxLayout()
    label_1 = SixthLabel()
    label_2 = SeventhLabel()
    label_3 = EighthLabel()
    label_4 = NinthLabel()
    label_5 = TenthLabel()

    box.add_widget(
        widget=label_1
    )
    box.add_widget(
        widget=label_2
    )
    box.add_widget(
        widget=label_3
    )
    box.add_widget(
        widget=label_4
    )
    box.add_widget(
        widget=label_5
    )

    ioc[SixthLabel] = label_1
    ioc[SeventhLabel] = label_2
    ioc[EighthLabel] = label_3
    ioc[NinthLabel] = label_4
    ioc[TenthLabel] = label_5
    ioc[SecondBoxLayout] = box

    widget.add_widget(
        widget=box
    )
