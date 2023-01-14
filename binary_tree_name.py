class BinaryNodeSearch:
    def __init__(self,DATA):
        self.DATA = DATA
        self.left = None
        self.right = None

    def plus_child(self, DATA):
        if DATA == self.DATA:
            return

        if DATA < self.DATA:
            if self.left:
                self.left.plus_child(DATA)
            else:
                self.left = BinaryNodeSearch(DATA)

        else:
            if self.right:
                self.right.plus_child(DATA)
            else:
                self.right = BinaryNodeSearch(DATA)

    def IN_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.IN_order_traversal()


        return elements
