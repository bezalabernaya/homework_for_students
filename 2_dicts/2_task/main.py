import re
def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    most_common = {}
    match_list = re.findall(r'\b\w{3,}\b', text.lower())
    for i in sorted(match_list):
        if i in most_common:
            most_common[i] += 1
        else:
            most_common[i] = 1
    return dict(sorted(most_common.items(), key=lambda x: x[1], reverse=True)[0:10])
