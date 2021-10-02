# Класс Ноды, для элементов списка
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_into_end_of_the_list(first, value):
    node = Node(value)
    if first is None:
        return node
    current = first
    while current.next is not None:
        current = current.next
    current.next = node
    return first


def insert_first(first, value):
    node = Node(value)
    node.next = first
    return node


def delete_first(first):
    if first is None:
        return None
    result = first.next
    del first
    return result


def delete_last(first):
    if first is None or first.next is None:
        return None
    current = first
    while current.next.next is not None:
        current = current.next
    to_be_deleted = current.next
    del to_be_deleted
    current.next = None
    return first


def print_list(first):
    # Выводим список
    print("!!!!!")
    current = first
    while current is not None:
        print(current.value)
        current = current.next
    print(current)  # None


# Первый элемент списка, важно не потерять его
first = Node(123)
print(first.value)
# Делается чтоб не потерять ссылку на первый
current = first
# current все еще ссылается на первый и изменения происходят в первом
current.value = 321
print(first.value)
# Генерируем список
for i in range(10):
    node = Node(i)
    current.next = node
    current = current.next

# first:   (321) -> (0) -> (1) -> (2) -> (3) -> (4) -> (5) -> (6) -> (7) -> (8) -> (9) -> None
# current: (321) -> (0) -> (1) -> (2) -> (3) -> (4) -> (5) -> (6) -> (7) -> (8) -> (9) -> None
# node:    (3) -> None
first = insert_into_end_of_the_list(first, 1000)

# Выводим список
print_list(first)
current = None
first = insert_into_end_of_the_list(current, 1111)

# Выводим список
print_list(first)

first = insert_first(first, 33)
print_list(first)

first = delete_first(first)
print_list(first)
first = delete_first(first)
print_list(first)
first = insert_first(first, 33)
first = insert_first(first, 32)
first = delete_last(first)
print_list(first)
