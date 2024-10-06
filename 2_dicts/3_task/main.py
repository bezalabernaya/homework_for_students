import re


def format_phone(phone_number: str) -> dict[str, int]:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """

    num = ''.join(re.findall(r'\d+', phone_number))

    if len(num) < 10:
        return phone_number
    else:
        formatted_phone_number = f"8 ({num[-10:-7]}) {num[-7:-4]}-{num[-4]}{num[-3]}-{num[-2]}{num[-1]}"
        return formatted_phone_number
