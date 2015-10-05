# -*- coding: utf-8 -*-


def edades(edad):
    """
    edades
    >>> edades(9)
    Eres nino

    """
    if edad < 0:
        print("No existes")
    elif edad < 13:
        print("Eres niño")
    elif edad < 18:
        print("Eres adolescente")
    elif edad < 65:
        print("Eres adulto")
    elif edad < 120:
        print("No existes")
    else:
        print("eres munra")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
