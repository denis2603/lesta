# coding=utf-8
import collections


class CircularBuffer:

    def __init__(self, size):
        self.__data = collections.deque(maxlen=size)

    def __repr__(self):
        return 'CircularBuffer({size})'.format(size=self.__data.maxlen)

    def __str__(self):
        return 'CircularBuffer({size}){data}'.format(size=self.__data.maxlen, data=str(list(self.__data)))

    def __len__(self):
        return len(self.__data)

    def push(self, value):
        """
        Добавить значение value в конец буфера. При превышении заданного размера самое старое значение удаляется.
        """
        self.__data.append(value)

    def pop(self):
        """
        Удаляет из буфера самый старый элемент и возвращает его значение.
        """
        if self.__data:
            return self.__data.popleft()
        else:
            raise IndexError('CircularBuffer is empty')

    def resize(self, new_size):
        """
        Изменить размер буфера. При уменьшении размера будут сохранены последние добавленные значения.
        """
        if new_size < self.__data.maxlen:
            self.__data = collections.deque(list(self.__data)[-new_size:], maxlen=new_size)

    @property
    def size(self):
        """
        Текущее значение размера буфера.
        """
        return self.__data.maxlen

    def clear(self):
        self.__data.clear()
