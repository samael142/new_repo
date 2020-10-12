def st(a, b):
    """

    :param a: Число (больше нуля)
    :param b: Степень возведения числа (Меньше нуля)
    :return: Число а в степени b
    """
    if a > 0 and b < 0:
        const_a = a
        for i in range(1, abs(b)):
            a = const_a * a
        return 1 / a
    else:
        return


print(st(5, -15))

# Через ** тоже умею :)
