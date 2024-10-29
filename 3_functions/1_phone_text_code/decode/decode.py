import sys
sys.path.append("..")
from dictionary import building_dict


def decode_numbers(numbers: str) -> str | None:

    dic = building_dict()
    result = ""
    for i in numbers.split():
        if i in dic:
            result += dic.get(i)
        else:
            return None

    return result

