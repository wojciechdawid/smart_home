def suma(collection: list | tuple | set | dict, cast_to_int: bool = False) -> int | float:  # noqa
    suma = 0.0
    if isinstance(collection, (list, tuple, set)):
        for i in collection:
            if isinstance(i, (int, float)):
                suma += i
            elif cast_to_int:
                try:
                    i = int(i)
                except ValueError:
                    continue
                else:
                    suma += i
    elif isinstance(collection, dict):
        for i in collection.values():
            if isinstance(i, (int, float)):
                suma += i
            elif cast_to_int:
                try:
                    i = int(i)
                except ValueError:
                    continue
                else:
                    suma += i
    else:
        raise TypeError("Bad input type")
    return suma
