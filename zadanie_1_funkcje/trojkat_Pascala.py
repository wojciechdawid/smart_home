from math import factorial


def pascal_triangle_row(n: int) -> list:
    return [factorial(n - 1) // (factorial(j) * factorial(n - 1 - j)) for j in range(n)]  # noqa


def pascal_triangle(n: int, to_str: bool = False) -> list | str:
    table = [pascal_triangle_row(j) for j in range(1, n + 1)]
    if not to_str:
        return table
    last_str = ''
    for i in range(n):
        last_str = last_str + f"{' ' * (n - i)}{' '.join([str(j) for j in table[i]])}{' ' * (n - i)}\n"  # noqa
    return last_str

print(pascal_triangle(7, to_str=True))