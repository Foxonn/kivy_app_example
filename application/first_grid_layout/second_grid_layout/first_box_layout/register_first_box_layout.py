from typing import (
    Any,
    Mapping,
)

from kivy.uix.widget import Widget

from .FirstBoxLayout import FirstBoxLayout
from .labels.FirstLabel import FirstLabel
from .labels.SecondLabel import SecondLabel
from .labels.ThirdLabel import ThirdLabel
from .labels.FourthLabel import FourthLabel
from .labels.FifthLabel import FifthLabel

__all__ = ['register_first_box_layout']


def register_first_box_layout(
    ioc: Mapping[str, Any],
    widget: Widget,
) -> None:
    box = FirstBoxLayout()
    label_1 = FirstLabel()
    label_2 = SecondLabel()
    label_3 = ThirdLabel()
    label_4 = FourthLabel()
    label_5 = FifthLabel()

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

    ioc[FirstLabel] = label_1
    ioc[SecondLabel] = label_2
    ioc[ThirdLabel] = label_3
    ioc[FourthLabel] = label_4
    ioc[FifthLabel] = label_5
    ioc[FirstBoxLayout] = box

    widget.add_widget(
        widget=box
    )
