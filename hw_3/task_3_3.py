import numpy as np

############ 1 часть: примесь ############

# Примесь в класс Matrix
class HashMixin:
    _cache = {}

    def __hash__(self):
        # Простейшая хэш-функция:
        # сумма всех элементов матрицы
        return int(np.sum(self.data))


    def _get_cached_matmul(self, second):
        key = (hash(self), hash(second))
        if key in self._cache:
            return self._cache[key]
        result = Matrix(self.data @ second.data)
        self._cache[key] = result
        return result
    
    
# Класс взял из 3.1
class Matrix(HashMixin):
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
    

############ 2 часть: поиск коллизий ############
np.random.seed(0)

def find_hash_collision():
    b = Matrix(np.random.randint(0, 5, (5, 5)))
    d = Matrix(np.copy(b.data))  # D = B

    while True:
        a_data = np.random.randint(0, 5, (5, 5))
        c_data = np.random.randint(0, 5, (5, 5))
        a = Matrix(a_data)
        c = Matrix(c_data)

        if hash(a) == hash(c) and not np.array_equal(a.data, c.data):
            ab = a @ b
            cd = c @ d
            if not np.array_equal(ab.data, cd.data):
                return a, b, c, d, ab, cd

a, b, c, d, ab, cd = find_hash_collision()

# Сохраняем файлы
a.to_file("A.txt")
b.to_file("B.txt")
c.to_file("C.txt")
d.to_file("D.txt")
ab.to_file("AB.txt")
cd.to_file("CD.txt")

with open("hash.txt", 'w') as f:
    f.write(f"hash(AB) = {hash(ab)}\n")
    f.write(f"hash(CD) = {hash(cd)}\n")