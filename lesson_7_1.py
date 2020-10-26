from random import randint


class MyMatrix:

    matrix_num = 0

    def __init__(self, length, elem):
        self.my_list = [[randint(10, 50) for el in range(elem)] for el1 in range(length)]

    def __add__(self, other):
        result = []
        for i in zip(self.my_list, other.my_list):
            temp_list = []
            for j in zip(i[0], i[1]):
                temp_list.append(sum(j))
            result.append(temp_list)
        return f"Сумма:     {result}"

    def __str__(self):
        MyMatrix.matrix_num += 1
        return f"Матрица {MyMatrix.matrix_num}: {self.my_list}"


a = MyMatrix(3, 4)
b = MyMatrix(3, 4)
print(a)
print(b)
print(a + b)
