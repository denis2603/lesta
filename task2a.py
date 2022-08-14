# coding=utf-8

class CircularBuffer:

    def __init__(self, size):
        self.__data = []
        self.__size = size

    def __repr__(self):
        return 'CircularBuffer({size})'.format(size=self.__size)

    def __str__(self):
        return 'CircularBuffer({size}){data}'.format(size=self.__size, data=str(self.__data))

    def __len__(self):
        return len(self.__data)

    def push(self, value):
        """
        Добавить значение value в конец буфера. При превышении заданного размера самое старое значение удаляется.
        """
        self.__data.append(value)
        if len(self.__data) > self.__size:
            self.__data.pop(0)

    def pop(self):
        """
        Удаляет из буфера самый старый элемент и возвращает его значение.
        """
        if self.__data:
            return self.__data.pop(0)
        else:
            raise IndexError('CircularBuffer is empty')

    def resize(self, new_size):
        """
        Изменить размер буфера. При уменьшении размера будут сохранены последние добавленные значения.
        """
        if new_size < self.__size:
            self.__data = self.__data[-new_size:]
        self.__size = new_size

    @property
    def size(self):
        """
        Текущее значение размера буфера.
        """
        return self.__size

    def clear(self):
        self.__data[:] = []
