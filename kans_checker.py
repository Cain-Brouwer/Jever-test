from typing import Any


def is_geldige_kans(
        x: float
) -> bool | Any:
        if 0 <= x <= 1:
            var = True
        else:
            var = False
        return var

def list_loop (
        numbers=None
):
    if numbers is None:
        numbers = [1, -0.2, 0, 1, 0.5, 0.4, 0.3, 0.2, 0.1]
    for number in numbers:
        if not is_geldige_kans(number):
            return False
    return True

print(is_geldige_kans(1.5))
print(list_loop())