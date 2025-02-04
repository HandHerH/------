class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class SingleLinkList:
    def __init__(self):
        self.head = None  # 默认head不存储数据

    def append_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = Node('head')
            self.head.next_node = new_node
            return True
        else:
            new_node.next_node = self.head.next_node
            self.head.next_node = new_node
            return True

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

    def add_at_target(self, target_data, data):
        new_node = Node(data)
        target_node = self.find_node(target_data)
        if not target_node:
            return False
        new_node.next_node = target_node.next_node
        target_node.next_node = new_node

    def find_node(self, target_data, last=False):
        if self.head is None:
            if last:
                return None, None
            return None

        last_node = None
        target_node = self.head

        while target_node.data != target_data:
            if target_node.next_node is None:
                break
            last_node = target_node
            target_node = target_node.next_node
        if last:
            return last_node, target_node
        return target_node

    def print_all_data(self):
        if self.head is None:
            return
        else:
            now_node = self.head
            while now_node.next_node is not None:
                print(now_node.data, end=' ')
                now_node = now_node.next_node
            print(now_node.data)

    def delete_target_node(self, target_data):
        last_node, target_node = self.find_node(target_data, last=True)
        if last_node is None:
            self.head = None
        else:
            last_node.next_node = target_node.next_node

    def reverse_list(self):
        if self.head is None:
            return True

        last_node = None
        now_node = self.head.next_node
        while now_node is not None:
            next_node = now_node.next_node
            now_node.next_node = last_node
            last_node = now_node
            now_node = next_node
        self.head.next_node = last_node


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    llist = SingleLinkList()
    for i in range(len(l)):
        llist.append_at_tail(l[i])
    # llist.print_all_data()
    # llist.append_at_head(1)
    # llist.print_all_data()
    # llist.add_at_target(4, 5)
    # llist.print_all_data()
    llist.reverse_list()
    llist.print_all_data()
