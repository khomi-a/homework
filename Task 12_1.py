import re


with open('input.txt', 'r', encoding='utf-8') as rf:
    for line in rf:
        print(*re.findall("\d+(?=₽)|\d+(?= ₽)|(?<=€)\d+|(?<=\$)\d+", line), end=' ')
