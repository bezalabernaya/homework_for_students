"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> bool:
    """Пишите ваш код здесь."""
    max_num = 0
    words = 0
    for i in sentences:
        for j in i.split():
            words += 1
        if words > max_num:
            max_num = words
        words = 0
    return max_num
