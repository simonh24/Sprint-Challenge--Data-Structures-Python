from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            return False

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        elif self.right is None:
            return self.value

    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        fn(self.value)

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    def bft_print(self):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    def dft_print(self):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
