from typing import Any

from dummy_predicter import output


def is_geldige_kans(
        x: float
) -> bool | Any:
    if 0 <= x <= 1:
        var = True
    else:
        var = False
    return var


def list_loop(
        numbers=None
):
    if numbers is None:
        numbers = output
    for number in numbers:
        if not is_geldige_kans(number):
            return False
    return True
