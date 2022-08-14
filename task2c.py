# coding=utf-8
class Unit:
    """
    Элемент буфера
    """
    def __init__(self, value):
        """
        :param value: данные, хранящиеся в элементе :arg value
        :arg self.next ссылка на следующий объект класса Unit, или None, если элемент последний в очереди
        """
        self.value = value
        self.next_item = None  # указатель на следующий элемент в очереди

    def __str__(self):
        return self.value

    def __repr__(self):
        return '{class_name}({value})'.format(class_name=self.__class__.__name__, value=self.value)


class CircularBuffer:

    def __init__(self, size):
        self.__first = None  # указатель на первый элемент
        self.__last = None  # указатель на последний элемент
        self.__count = 0  # количество элементов в буфере
        self.__size = size

    def __repr__(self):
        return 'CircularBuffer({size})'.format(size=self.__size)

    def __str__(self):
        values = []
        current_unit = self.__last
        while current_unit is not None:
            values.append(current_unit.value)
            current_unit = current_unit.next_item
        return 'CircularBuffer({size}){data}'.format(size=self.__size, data=values)

    def __len__(self):
        return self.__count

    def push(self, value):
        """
        Добавить значение value в начало буфера. При превышении заданного размера самое старое значение удаляется.
        """
        if self.__count == 0:  # очередь пуста
            self.__last = self.__first = Unit(value)
        else:
            assert self.__first.next_item is None, 'Должен быть последний элемент, а это не последний'
            self.__first.next_item = Unit(value)
            self.__first = self.__first.next_item

        if self.__count == self.__size:
            self.__last = self.__last.next_item
        else:
            self.__count += 1

    def pop(self):
        """
        Удаляет из буфера самый старый элемент и возвращает его значение.
        """
        if self.__count == 0:
            raise IndexError('CircularBuffer is empty')
        current_unit = self.__last
        self.__last = self.__last.next_item
        self.__count -= 1
        return current_unit.value

    def resize(self, new_size):
        """
        Изменить размер буфера. При уменьшении размера будут сохранены последние добавленные значения.
        """
        if new_size < self.__count:
            for _ in range(self.__count - new_size):
                self.__last = self.__last.next_item
            self.__count = new_size
        self.__size = new_size

    @property
    def size(self):
        """
        Текущее значение размера буфера.
        """
        return self.__size

    def clear(self):
        self.__init__(self.__size)
