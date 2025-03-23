import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
    

    def __add__(self, second):
        if self.data.shape != second.data.shape:
            raise ValueError("Матрицы должны быть одинаковой размерности")
        return Matrix(self.data + second.data)


    def __mul__(self, second):
        if self.data.shape != second.data.shape:
            raise ValueError("Матрицы должны быть одинаковой размерности")
        return Matrix(self.data * second.data)


    def __matmul__(self, second):
        if self.data.shape[1] != second.data.shape[0]:
            raise ValueError("Матрицы должны быть подходящей размерности")
        return Matrix(self.data @ second.data)


    def __str__(self):
        return str(self.data)


    def to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')

# Генерация матриц
np.random.seed(0)
m1 = Matrix(np.random.randint(0, 10, (10, 10)))
m2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Операции
m_add = m1 + m2
m_mul = m1 * m2
m_matmul = m1 @ m2

# Запись в файлы
m_add.to_file("matrix+.txt")
m_mul.to_file("matrix_mul.txt")
m_matmul.to_file("matrix_matmul.txt")