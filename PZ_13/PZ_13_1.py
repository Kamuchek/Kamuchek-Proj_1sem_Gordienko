# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива

# pip install numpy  надо ввести команду в терминале перед запуском кода
import numpy as np

matrix = np.array([[1, 2, -3], [4, -5, 6], [-7, 8, 9]])
negative_elements = [x for sublist in matrix for x in sublist if x < 0]

print("отрицательные элементы:", negative_elements)
print("Размер нового массива:", len(negative_elements))