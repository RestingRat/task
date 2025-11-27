class Queue:
    def __init__(self):
        self._items = []  # внутреннее хранилище

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)  # удаляем первый элемент

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._items[0]

    # Только для отладки (не используется в логике)
    def to_list(self):
        return self._items[:]


def remove_consecutive_duplicates(queue):
    if queue.is_empty():
        return

    # Вспомогательная очередь для результата
    result_queue = Queue()

    # Берём первый элемент
    prev = queue.dequeue()
    result_queue.enqueue(prev)

    # Обрабатываем оставшиеся
    while not queue.is_empty():
        current = queue.dequeue()
        if current != prev:
            result_queue.enqueue(current)
            prev = current
        # если current == prev — пропускаем (удаляем дубликат)

    # Копируем результат обратно в исходную очередь
    while not result_queue.is_empty():
        queue.enqueue(result_queue.dequeue())


# Пример использования:
if __name__ == "__main__":
    q = Queue()
    input_str = input("Введите строку символов (например, aabbbcaa): ").strip()
    for ch in input_str:
        q.enqueue(ch)

    print("Исходная очередь:", q.to_list())

    remove_consecutive_duplicates(q)

    print("Очередь после удаления подряд идущих дубликатов:", q.to_list())