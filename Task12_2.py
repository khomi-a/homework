import re


books = []
with open('input2.txt', 'r', encoding='utf-8') as rf:
    for line in rf:
        books.append(re.findall('(?<=чита. )[\w+ ]+(?=[!])|(?<=книг. )[\w+ ]+(?=[!])', line))
        books.append(re.findall('(?<=книг. )«([\w ]+)»|(?<=чита. )«([\w ]+)»', line))
print(books)