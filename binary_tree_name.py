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

        elements.append(self.DATA)

        if self.right:
            elements += self.right.IN_order_traversal()

        return elements

    def search_scan(self,item):
        if self.DATA == item:
            return True

        if item < self.DATA:
            if self.left:
                return self.left.search_scan(item)
            else:
                return False

        if item > self.DATA :
            if self.right:
                return self.right.search_scan(item)
            else:
                return False 

    def deleter(self,item):
        if item < self.DATA:
            if self.left:
                self.left = self.left.deleter(item)
        elif item > self.DATA:
            if self.right:
                self.right = self.right.deleter(item)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_item_val = self.left.find_max()
            self.DATA = max_item_val
            self.left = self.left.delete(max_item_val)
        return self

    def find_max(self):
        if self.right is None:
            return self.DATA
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.DATA
        return self.left.find_min()
    
def tree_builder(elements):
    root = BinaryNodeSearch(elements[0])

    for iter in range(1,len(elements)):
        root.plus_child(elements[iter])
    return root

if __name__ == '__main__':
    name_letter = ["C","H","R","I","S","T","I","A","N","K","E","V","I","N","P","E","L","I","P","A","D","A","D","E","V","E","G","A"]
    nl_tree = tree_builder(name_letter)

    print("In Order Traversal: ",nl_tree.IN_order_traversal())
    print("Search: ",nl_tree.search_scan("R"))
    print("Minimum value: ",nl_tree.find_min())
    print("Maximum value: ",nl_tree.find_max())



        



