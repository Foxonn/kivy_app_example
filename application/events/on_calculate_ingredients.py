from functools import partial
from typing import (
    Any,
    Mapping
)

from kivy.uix.textinput import TextInput

from application.first_grid_layout.first_anchor_layout.inputs.FirstInput import (
    FirstInput
)
from application.first_grid_layout.fourth_box_layout.buttons.FirstButton import (
    FirstButton
)
from application.first_grid_layout.second_grid_layout.second_box_layout.labels.EighthLabel import (
    EighthLabel
)
from application.first_grid_layout.second_grid_layout.second_box_layout.labels.NinthLabel import (
    NinthLabel
)
from application.first_grid_layout.second_grid_layout.second_box_layout.labels.SeventhLabel import (
    SeventhLabel
)
from application.first_grid_layout.second_grid_layout.second_box_layout.labels.SixthLabel import (
    SixthLabel
)
from application.first_grid_layout.second_grid_layout.second_box_layout.labels.TenthLabel import (
    TenthLabel
)
from application.services.calculate_ingredients import calculate_ingredients

__all__ = ['on_calculate_ingredients']


def on_calculate_ingredients(
    ioc: Mapping[str, Any]
) -> None:
    button = ioc[FirstButton]
    input = ioc[FirstInput]

    def release(input: TextInput) -> None:
        try:
            value = int(input.text)
        except ValueError as err:
            print(err)
        else:
            calculate = calculate_ingredients(value)
            ioc[SixthLabel].text = f"{calculate['nitro']} + 5"
            ioc[SeventhLabel].text = calculate['salt']
            ioc[EighthLabel].text = calculate['stats']
            ioc[NinthLabel].text = calculate['dextrose']
            ioc[TenthLabel].text = calculate['salting_time']

    setattr(
        button,
        'on_release',
        partial(
            release,
            input
        )
    )
