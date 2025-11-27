class Stack:
    def __init__(self):
        self._items = []  # внутреннее хранилище (реализация на базе списка)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    # Вспомогательный метод для отладки (необязательный)
    def __repr__(self):
        return f"Stack({self._items})"


def main():
    # Ввод данных
    N = int(input("Введите N (количество чисел в стеке): "))
    K = int(input("Введите K (сколько первых чисел суммировать): "))

    if K > N or K <= 0:
        print("Некорректное значение K. Должно быть 1 <= K <= N.")
        return

    # Создание стека и заполнение N числами
    stack = Stack()
    print(f"Введите {N} чисел:")
    for _ in range(N):
        num = int(input())
        stack.push(num)

    # Извлечение всех элементов из стека в обратном порядке (т.к. стек — LIFO)
    # Чтобы получить "первые K чисел", введённых пользователем,
    # нужно временно переложить всё в доп. стек
    temp_stack = Stack()
    original_numbers = []

    # Извлекаем всё из основного стека и запоминаем порядок ввода
    while not stack.is_empty():
        val = stack.pop()
        temp_stack.push(val)
        original_numbers.append(val)

    # Восстанавливаем исходный стек в правильном порядке (как было)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    # Теперь original_numbers содержит числа в порядке от последнего введённого к первому
    # То есть: original_numbers[0] — последнее введённое, original_numbers[N-1] — первое введённое
    # Чтобы получить "первые K введённых чисел", нужно взять последние K элементов из original_numbers
    first_k_numbers = original_numbers[-K:]

    sum_k = sum(first_k_numbers)

    # Помещаем результат (сумму) в стек
    stack.push(sum_k)

    print(f"Сумма первых {K} чисел: {sum_k}")
    print("Текущее содержимое стека (снизу вверх):")
    # Для вывода стека без разрушения — используем временный стек
    display_temp = Stack()
    while not stack.is_empty():
        display_temp.push(stack.pop())

    output = []
    while not display_temp.is_empty():
        val = display_temp.pop()
        output.append(val)
        stack.push(val)  # восстанавливаем

    print(output)


if __name__ == "__main__":
    main()