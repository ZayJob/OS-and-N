class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None

class Tree():
    def __init__(self):
        self.tree = Node()


    def add(self, number, node):
        if node.right is not None:
            if number >= node.data:
                self.add(number, node.right)
                return
        if node.left is not None:
            if number < node.data:
                self.add(number, node.left)
                return

        if node.data is None:
            node.data = number
        else:
            new_node = Node()
            new_node.data = number
            new_node.parent = node
            if number >= node.data:
                node.right = new_node
            else:
                node.left = new_node


    def find_left(self, node):
        if node.left is None:
            return node
        else:
            return self.find(node.left)


    def find(self, data, node):
        if data == node.data:
            return node

        if data > node.data:
            return self.find(data, node.right)
        else:
            return self.find(data, node.left)


    def remove(self, node):
        if node.left is None and node.right is None:
            if node.data > node.parent.data:
                node.parent.right = None
            else:
                node.parent.left = None
            return

        if node.left is None or node.right is None:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if node.data > node.parent.data:
                node.parent.right = child
                child.parent = node.parent.right
            else:
                node.parent.left = child
                child.parent = node.parent.left
            return

        if node.right.left is None:
            if node.data > node.parent.data:
                node.parent.right = node.right.left
                node.right.left = node.parent.right
            else:
                node.parent.left = node.right.left
                node.right.left = node.parent.left
            node.right.left = node.left
        else:
            most_left = self.find_left(node.right)
            node.data = most_left.data
            self.remove(most_left)


    def clear(self):
        self.tree = Node()


    def show(self, node):
        right_data = ""
        if node.right is not None:
            right_data = node.right.data
        left_data = ""
        if node.left is not None:
            left_data = node.left.data
        print("{0} [{1}, {2}]".format(node.data, left_data, right_data))
        if node.right is not None:
            self.show(node.right)
        if node.left is not None:
            self.show(node.left)
    
    def event_menu(self, action):
            if action == 1:
                data = input("Data: ")
                self.add(data, self.tree)
            elif action == 2:
                data = input("Data: ")
                node = self.find(data, self.tree)
                self.remove(node)
            elif action == 3:
                self.clear()
            elif action == 4:
                self.show(self.tree)
            else:
                print("Not found event")
            


def main():
    try:
        tree = Tree()
        action = None
        while action != 0:
            action = input("1 - add\n2 - remove\n3 - clear\n4 - show\n0 - exit: ")
            tree.event_menu(int(action))
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()