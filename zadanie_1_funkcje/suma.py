def suma(collection: list | tuple | set | dict, cast_to_int: bool = False) -> int | float:  # noqa
    suma = 0.0
    if isinstance(collection, (list, tuple, set)):
        coll = collection
    elif isinstance(collection, dict):
        coll = collection.values()
    else:
        raise TypeError("Bad input type")
    for i in coll:
        if isinstance(i, (int, float)):
            suma += i
        elif cast_to_int:
            try:
                i = int(i)
                suma += i
            except ValueError:
                continue
    return suma
