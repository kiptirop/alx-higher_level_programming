#!/usr/bin/python3

"""defines multiplication of 2 matrices"""

def matrix_mul(m_a, m_b):
    """multiplies two matrices"""

    # Validate m_a and m_b
    for m in [m_a, m_b]:
        if not isinstance(m, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if not all(isinstance(row, list) for row in m):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
        if not m:
            raise ValueError("m_a can't be empty or m_b can't be empty")
        if not all(isinstance(num, (int, float)) for row in m for num in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
        if len(set(len(row) for row in m)) != 1:
            raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate that m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute the product of m_a and m_b
    product = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                product[i][j] += m_a[i][k] * m_b[k][j]

    return product
