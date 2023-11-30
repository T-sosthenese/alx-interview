from math import factorial


def pascal_triangle(n):
    """A function that computes Pascal's triangle coefficients."""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [factorial(i)//(factorial(j)*factorial(i-j)) for j in range(i+1)]
        triangle.append(row)

    return triangle
