def karatsuba(x, y):
    '''
    :param x: positive integer with n digits
    :param y: positive integer with n digits
    :return: the product of x and y
    '''
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y)))

        a = x // 10 ** (m // 2)
        b = x % 10 ** (m // 2)
        c = y // 10 ** (m // 2)
        d = y % 10 ** (m // 2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return (ac * 10 ** (2 * (m // 2))) + (ad_plus_bc * 10 ** (m // 2)) + bd

print(karatsuba(1234, 5678))