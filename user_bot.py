def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        if check("wall", x + 2, y):
            return "down"
        else:
            return "right"
    return "pass"
