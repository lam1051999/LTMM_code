def inv_number_modulo(a, m):
    if a < 0:
        a = a % m
    if a == 0:
        raise Exception("{} is divisible by {}".format(a, m))
    r1 = m
    r2 = a
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = int(r1 // r2)
        r = r1 - q*r2
        r1 = r2
        r2 = r
        t = t1 - q*t2
        t1 = t2
        t2 = t

    if r1 == 1:
        return t1
    else:
        raise Exception("Cannot find the inverse of {} mod {}".format(a, m))
