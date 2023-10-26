class Node:
  """
  Вспомогательный класс для узлов списка
  """

  def __init__(self, data):
    self.data = data  # храним информацию
    self.next = None  # ссылка на следующий узел


class Stack:
  """
  Основной класс для стека на основе односвязного списка
  """

  def __init__(self):
    self.top = None  # ссылка на вершину стека

  def pop(self):
    """
    Возвращает последний элемент из стека с удалением его из стека
    """
    if self.is_empty():
      raise Exception("Stack is empty")
    value = self.top.data
    self.top = self.top.next
    return value

  def push(self, value):
    """
    Добавляет элемент value в вершину стека
    """
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node

  def print(self):
    """
    Выводит на печать содержимое стека
    """
    current = self.top
    while current:
      print(current.data)
      current = current.next

  def is_empty(self):
    """
    Проверяет, пуст ли стек
    """
    return self.top is None
