# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count = 0
for i in word.lower():
    if i in vowels:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = 0
for i in sentence.split():
    words += len(i)
print(words / len(sentence.split()))