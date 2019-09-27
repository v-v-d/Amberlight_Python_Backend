"""
Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что
вы не считаете знаки препинания, цифры и пробелы, а только буквы.
Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
"""

from collections import Counter


def get_sorted_letters(text, from_symbol, to_symbol):
    sorted_letters_list = [l for l in text.lower() if ord(l) in range(from_symbol, to_symbol + 1)]
    sorted_letters = ''.join(sorted(sorted_letters_list))
    return sorted_letters


random_text = '''
Here you can find activities to practise your reading skills. Reading will help you to improve your understanding of
the language and build your vocabulary. The self-study lessons in this section are written and organised according to
the levels of the Common European Framework of Reference for languages (CEFR). There are different types of texts and
interactive exercises that practise the reading skills you need to do well in your studies, to get ahead at work and to
communicate in English in your free time. Take our free online English test to find out which level to choose. Select
your level, from beginner (CEFR level A1) to advanced (CEFR level C1), and improve your reading skills at your own
speed, whenever it's convenient for you.
'''

first_ascii_code = 97
last_ascii_code = 122

cleaned_sorted_text = get_sorted_letters(random_text, first_ascii_code, last_ascii_code)

most_common_letter = Counter(cleaned_sorted_text).most_common(1)[0][0]

print(most_common_letter)
