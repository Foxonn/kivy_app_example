from typing import (
    Any,
    Mapping,
)

from kivy.app import App

from application.MyApp import MyApp
from application.events.on_calculate_ingredients import (
    on_calculate_ingredients
)
from application.first_grid_layout.first_anchor_layout.inputs.FirstInput import \
    FirstInput
from application.first_grid_layout.first_anchor_layout.register_first_anchor_layout import (
    register_first_anchor_layout
)
from application.first_grid_layout.fourth_box_layout.register_fourth_box_layout import (
    register_fourth_box_layout
)
from application.first_grid_layout.second_grid_layout.register_second_grid_layout import (
    register_second_grid_layout
)

__all__ = ['build_app']


class FoodManager(App):
    pass


def build_app(
    app: MyApp,
    ioc: Mapping[str, Any]
) -> App:
    register_first_anchor_layout(
        ioc=ioc,
        widget=app.container
    )
    register_second_grid_layout(
        ioc=ioc,
        widget=app.container
    )
    register_fourth_box_layout(
        ioc=ioc,
        widget=app.container
    )
    on_calculate_ingredients(ioc=ioc)

    return app
