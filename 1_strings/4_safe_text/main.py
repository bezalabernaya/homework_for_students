import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()

    # Ваш код ниже, возвращайте уже отредактированный текст!
    sentences = [i for i in wrong_article.split('\n')]
    norm_sen = ['' for i in range(len(sentences))]
    for j in range(len(sentences)):
        for k in sentences[j][int(len(sentences[j]) / 2) - 1::-1]:
            norm_sen[j] += k.lower()
        norm_sen[j] = norm_sen[j].replace("woof-woof", "cat").capitalize()

    return ".\n".join(norm_sen)
