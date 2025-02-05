class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class IterLinkList:
    def __init__(self, node):
        self.curr_node = node
        self.return_node = None

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        self.return_node, self.curr_node = self.curr_node, self.curr_node.next_node
        return self.return_node

    def __iter__(self):
        return self


class SingleLinkList:
    def __init__(self):
        self.head = None  # 默认head不存储数据

    def __iter__(self):
        return IterLinkList(self.head)

    def append_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = Node('head')
            self.head.next_node = new_node
            return True
        else:
            tail_node = self.head
            while tail_node.next_node is not None:
                tail_node = tail_node.next_node
            tail_node.next_node = new_node
            return True


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    llist = SingleLinkList()
    for i in range(len(l)):
        llist.append_at_tail(l[i])

    for i in llist:
        print(i.data, end=' ')
