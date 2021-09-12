from typing import Mapping


def calculate_ingredients(value: int) -> Mapping[str, str]:
    return {
        'nitro': str(10 * value / 1000),
        'salt': str(15 * value / 1000),
        'stats': str(.5 * value / 1000),
        'dextrose': str(5 * value / 1000),
        'salting_time': str(round(value / 500 * 2)),
    }
