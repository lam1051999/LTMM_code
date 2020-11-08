def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    return True
