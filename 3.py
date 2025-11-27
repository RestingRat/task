class CharSet:
    def __init__(self):
        self._elements = []  # список для хранения уникальных символов

    def add(self, ch):
        # Проверяем, есть ли уже такой элемент — вручную
        for elem in self._elements:
            if elem == ch:
                return  # уже есть — не добавляем
        self._elements.append(ch)

    def to_list(self):
        return self._elements[:]  # копия для вывода

    def size(self):
        return len(self._elements)


def is_lowercase_latin(ch):
    return 'a' <= ch <= 'z'


def is_punctuation(ch):
    # Определим знаки препинания как всё, что не буква, не цифра и не пробел/таб/перевод строки
    # Можно расширить по желанию
    if ch.isalpha() or ch.isdigit() or ch.isspace():
        return False
    return True


def main():
    s = input("Введите строку: ")

    letters_set = CharSet()
    punctuation_count = 0

    for ch in s:
        if is_lowercase_latin(ch):
            letters_set.add(ch)
        if is_punctuation(ch):
            punctuation_count += 1

    # Вывод результата
    letters = sorted(letters_set.to_list())  # сортируем для красивого вывода
    print("Множество строчных латинских букв:", ''.join(letters))
    print("Количество знаков препинания:", punctuation_count)


if __name__ == "__main__":
    main()