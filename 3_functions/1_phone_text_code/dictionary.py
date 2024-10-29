def building_dict() -> dict:
    alphabet = '.,?!:;абвгдежзийклмнопрстуфхцчшщъыьэюя'
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
