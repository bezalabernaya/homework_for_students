def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""

    a = ord('а')

    alphabet = '.,?!:;'
    alphabet += ''.join([chr(i) for i in range(a, a + 32)])

    d = {' ': '0'}

    counter = 0
    num = 1
    for t in alphabet:
        counter += 1
        d[t] = str(num) * counter
        if num == 1 and counter == 6 or num != 1 and counter == 4:
            counter = 0
            num += 1
            continue

    result = ""
    for i in text:
        if i in d:
            result += d.get(i)+' '
        else:
            return None

    return result[:-1]

