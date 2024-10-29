import sys
sys.path.append("..")
from dictionary import building_dict


def decode_numbers(numbers: str) -> str | None:

    d = building_dict()
    result = ""
    for i in numbers.split():
        if i in d:
            result += d.get(i)
        else:
            return None

    return result

