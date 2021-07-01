from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
    print(matrix1, '\n')

    matrix2 = Matrix([[3, 5], [2, 4], [-1, 64]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
