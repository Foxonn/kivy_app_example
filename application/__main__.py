from typing import (
    Any,
    Mapping
)

from application.MyApp import MyApp
from application.build_app import build_app
from application.config import load_config

if __name__ == '__main__':
    load_config()
    app = MyApp()
    ioc: Mapping[str, Any] = {}

    build_app(
        app=app,
        ioc=ioc
    )

    app.run()
