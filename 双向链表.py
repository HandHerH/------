class Node:
    def __init__(self, data=None, next_node=None, pre_node=None):
        self.data = data
        self.next_node = next_node
        self.pre_node = pre_node


class DoubleLinkList:
    def __init__(self):
        self.head = None  # 可以存储数据
        self.tail = None

    def append_at_head(self, data=None):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = self.head
            return True
        if self.head == self.tail:
            self.head = node
            self.head.next_node = self.tail
            self.tail.pre_node = self.head
            return True
        else:
            node.next_node = self.head
            self.head.pre_node = node
            self.head = node
            return True

    def append_at_tail(self, data=None):
        node = Node(data=data)
        if self.tail is None:
            self.tail = node
            self.head = self.tail
            return True
        elif self.tail == self.head:
            self.tail = node
            self.head.next_node = self.tail
            self.tail.pre_node = self.head
            return True
        else:
            node.pre_node = self.tail
            self.tail.next_node = node
            self.tail = node
            return True

    def find_node(self, data=None):
        if self.head is None:
            return None
        elif self.head == self.tail:
            if self.head.data == data:
                return self.head
        else:
            now_node = self.head
            while now_node is not None:
                if now_node.data == data:
                    return now_node
                now_node = now_node.next_node
            return None

    def delete_node(self, data=None):
        node = self.find_node(data)
        if node is None:
            return False
        if self.head == self.tail:
            self.head, self.tail = None, None
        elif node == self.head:
            self.head = node.next_node
            self.head.pre_node = None
        elif self.tail == node:
            self.tail = node.pre_node
            self.tail.next_node = None
        else:
            node.pre_node.next_node = node.next_node
            node.next_node.pre_node = node.pre_node

        return True

    def from_head_data(self):
        if self.head is None:
            return
        now_node = self.head
        while now_node.next_node is not None:
            print(now_node.data, end=' ')
            now_node = now_node.next_node
        print(now_node.data)

    def from_tail_data(self):
        if self.tail is None:
            return
        now_node = self.tail
        while now_node.pre_node is not None:
            print(now_node.data, end=' ')
            now_node = now_node.pre_node
        print(now_node.data)


if __name__ == '__main__':
    ll = DoubleLinkList()
    for i in range(1, 2):
        ll.append_at_tail(i)
    ll.from_head_data()
    ll.delete_node(1)
    ll.from_head_data()
