# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#           Содержимое первого файла:
#           Элементы кратные 3:
#       Произведение элементов:
#           Минимальный элемент:
#           Содержимое второго файла:
#           Элементы кратные 5:
#           Количество элементов:
#           Среднее арифметическое элементов:

# записываем первую последовательность положительных чисел в file1.txt
with open("file1.txt", "w") as file1:
    file1.write("1 2 3 4 5 6 7 8 9 10")

# записываем вторую последовательность отрицательных чисел в file2.txt
with open("file2.txt", "w") as file2:
    file2.write("-1 -2 -3 -4 -5 -6 -7 -8")

# обрабатываем элементы из обоих файлов и записывайте в file3.txt
with open("file3.txt", "w") as file3:
    # элементы процесса из file1.txt
    with open("file1.txt") as file1:
        positive_numbers = [int(x) for x in file1.read().split()]
        multiple_of_3 = [x for x in positive_numbers if x % 3 == 0]
        product_of_elements = 1
        for x in positive_numbers:
            product_of_elements *= x
        file3.write("Содержимое первого файла:\n")
        file3.write("Элементы, кратные 3: {}\n".format(multiple_of_3))
        file3.write("Произведение элементов: {}\n".format(product_of_elements))
        file3.write("Минимальный элемент: {}\n".format(min(positive_numbers)))
    # элементы процесса из file2.txt
    with open("file2.txt") as file2:
        negative_numbers = [int(x) for x in file2.read().split()]
        multiple_of_5 = [x for x in negative_numbers if x % 5 == 0]
        count_of_elements = len(negative_numbers)
        average_of_elements = sum(negative_numbers) / count_of_elements
        file3.write("Содержимое второго файла:\n")
        file3.write("Элементы, кратные 5: {}\n".format(multiple_of_5))
        file3.write("Количество элементов: {}\n".format(count_of_elements))
        file3.write("Среднее значение элементов: {}\n".format(average_of_elements))

