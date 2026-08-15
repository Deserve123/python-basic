class SingleNode:
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkedList:
    def __init__(self,node=None):
        self.head = node

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        # return True if self.head is None else False 三元运算
        # return self.head is None
        
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head        
        while cur is not None:
            print(f'数值域:{cur.item}')            
            cur = cur.next

    def add(self,item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        

    def insert(self,pos,item):
        if pos<=0:
            self.add()
        elif pos>=self.length():
            self.append()
        else:
            cur = self.head
            count = 0
            while count<pos-1:
                cur = cur.next
                count += 1
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node

    def remove(self,item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next                   
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.head
        while cur is not None: 
            if cur.item == item:
                return True
            cur = cur.next
        return False
            


if __name__ == '__main__':
    node1 = SingleNode()
    ll1 = SingleLinkedList(node1)
   
    print(f'{ll1.is_empty()}')
    print('-'*27)

    ll1.add()
    ll1.append()
    

    print('-'*27)
    print(f'链表的长度:{ll1.length()}')

    print('-'*27)
    ll1.travel()

    