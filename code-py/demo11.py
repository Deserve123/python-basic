class Node:
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self,node=None):
        self.root = node

    def add(self,item):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return
        queue = []
        queue.append(self.root)
        while True:
            node = queue.pop(0)
            if node.lchild is None:
                node.lchild = new_node
                return
            else:
                queue.append(node.lchild)
            if node.rchild is None:
                node.rchild = new_node
                return
            else:
                queue.append(node.rchild)

    #广度优先算法
    def breadth(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.item,end='')
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    #深度优先算法 先序 中序 后序
    def preorder(self,root):
        if root is not None:
            print(root.item,end='')
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self,root):
        if root is not None:
            self.preorder(root.lchild)
            print(root.item,end='')
            self.preorder(root.rchild)
            
    def postorder(self,root):
         if root is not None:
            self.preorder(root.lchild)           
            self.preorder(root.rchild)
            print(root.item,end='')

if __name__ == '__main__':
     
    tr1 = BinaryTree()
    tr1.add()