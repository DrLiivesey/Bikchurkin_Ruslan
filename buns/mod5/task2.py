class Node:
  """
  Вспомогательный класс для узлов списка
  """

  def __init__(self, data):
    self.data = data  # храним информацию
    self.next = None  # ссылка на следующий узел
    self.prev = None  # ссылка на предыдущий узел


class Queue:
  """
  Основной класс для очереди на основе двусвязного списка
  """

  def __init__(self):
    self.start = None  # ссылка на начало очереди
    self.end = None  # ссылка на конец очереди

  def pop(self):
    """
    Возвращает первый элемент из очереди с удалением его из очереди
    """
    if self.is_empty():
      raise Exception("Queue is empty")
    value = self.start.data
    self.start = self.start.next
    if self.start is None:
      self.end = None
    else:
      self.start.prev = None
    return value

  def push(self, value):
    """
    Добавляет элемент value в конец очереди
    """
    new_node = Node(value)
    if self.is_empty():
      self.start = new_node
      self.end = new_node
    else:
      new_node.prev = self.end
      self.end.next = new_node
      self.end = new_node

  def insert(self, n, value):
    """
    Вставляет элемент value между элементами с номерами n-1 и n
    """
    new_node = Node(value)
    if n == 0:
      new_node.next = self.start
      if self.start is None:
        self.end = new_node
      else:
        self.start.prev = new_node
      self.start = new_node
    else:
      current = self.start
      for i in range(n - 1):
        if current is None:
          raise Exception("Index out of range")
        current = current.next
      if current is None:
        raise Exception("Index out of range")
      new_node.prev = current
      new_node.next = current.next
      if current.next is None:
        self.end = new_node
      else:
        current.next.prev = new_node
      current.next = new_node

  def print(self):
    """
    Выводит на печать содержимое очереди
    """
    current = self.start
    while current:
      print(current.data)
      current = current.next

  def is_empty(self):
    """
    Проверяет, пуста ли очередь
    """
    return self.start is None
