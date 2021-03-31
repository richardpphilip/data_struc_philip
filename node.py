class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False
