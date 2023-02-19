def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y) != 0:
            return "take"
        if check("wall", x + 2, y):
            return "down"
        else:
            return "right"
    elif check("level") == 2:
        if check("gold", x, y) != 0:
            return "take"
        if check("wall", x + 2, y) is False and check("wall", x, y + 1):
            return "right"
        if check("gold", x, y + 1) != 0:
            return "down"
        if check("wall", x, y - 1) is False:
            return "up"
        return "right"
    return "pass"
