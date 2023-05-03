# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов

import re

years = []
with open("Dostoevsky.txt", "r", encoding="UTF-8") as file:
    text = file.read()
    matches = re.findall(r"\b\d{4}\b", text)
    for match in matches:
        years.append(int(match))

print("Кол-во годов:", len(years))
print("Года:", years)

# код находит все годы в текстовом файле "Dostoevsky.txt" и подсчитывает количество найденных элементов