class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
        
           self.simetric_traversal(node.left)
       
        if node.right:
            self.simetric_traversal(node.right)
         

    def posOrdem_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.posOrdem_traversal(node.left)
        if node.right:
            self.posOrdem_traversal(node.right)
        print(node)

    def height(self, node=None):
        if node is None:
            node = self.root
        height_left = 0
        height_right = 0

        if node.left:
            height_left = self.height(node.left)

        if node.right:
            height_right = self.height(node.right)
        
        if height_right > height_left:
            return height_right + 1
        return height_left + 1
        
        
def posOrder_example_tree():
    tree = BinaryTree()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n0 = Node(10)

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.left = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


if __name__ == "__main__":
    tree = posOrder_example_tree()
    print("Percuso pós ordem:")
    tree.posOrdem_traversal()
    print("Altura:", tree.height())
    

   
  