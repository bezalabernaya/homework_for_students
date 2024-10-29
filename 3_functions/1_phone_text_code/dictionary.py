def building_dict() -> dict:
    a = ord('а')
    alphabet = '.,?!:;'
    alphabet += ''.join([chr(i) for i in range(a, a + 32)])
    d = {'0': ' '}
    counter = 0
    num = 1
    for t in alphabet:
        counter += 1
        d[str(num) * counter] = t
        if num == 1 and counter == 6 or num != 1 and counter == 4:
            counter = 0
            num += 1
            continue

    return d
