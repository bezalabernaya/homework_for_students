import sys
sys.path.append("..")
from dictionary import building_dict


def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    d = {v: k for k, v in building_dict().items()}
    result = ""
    for i in text:
        if i in d:
            result += d.get(i)+' '
        else:
            return None

    return result[:-1]

