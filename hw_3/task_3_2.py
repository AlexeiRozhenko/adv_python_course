import numpy as np

# Арифметические операции
class ArithmeticMixin:
    def __add__(self, second):
        return self.__class__(self.data + second.data)

    def __sub__(self, second):
        return self.__class__(self.data - second.data)

    def __mul__(self, second):
        return self.__class__(self.data * second.data)

    def __truediv__(self, second):
        return self.__class__(self.data / second.data)

    def __matmul__(self, second):
        return self.__class__(self.data @ second.data)

# Красивый вывод
class StringMixin:
    def __str__(self):
        return str(self.data)

# Геттеры и сеттеры
class AccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

# Запись в файл
class FileMixin:
    def to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')

# Базовый класс
class Matrix(ArithmeticMixin, StringMixin, FileMixin, AccessMixin):
    def __init__(self, data):
        self.data = data

# Генерация матриц
np.random.seed(0)
m1 = Matrix(np.random.randint(0, 10, (10, 10)))
m2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Операции
m_add = m1 + m2
m_mul = m1 * m2
m_matmul = m1 @ m2

# Сохранение
m_add.to_file("matrix_+.txt")
m_mul.to_file("matrix_mul.txt")
m_matmul.to_file("matrix_matmul.txt")
