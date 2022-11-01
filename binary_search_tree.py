### What is the time complexity to retrieve a value?

#### Time complexity for the worst case scenario to search an object is O(n), since it is needed to iterate through the entire tree to get the value. This would be the case for a linear tree.
#### In the average and best case scenario, time complexity is O(log n). As an example, if we double the size, the time will only increase one half.

### Does it matter in what order values are inserted?
#### It does matter, as depending on the order of the insertion, the tree will be build in a balance or unbalanced way. This will strongly affect the time complexity of the posterior search. 
#### As an example for this case, if we start the tree with a name starting with "Z", we will end up with a left sided tree. On the other hand, if we allways use names located in the middle we will get a more balance tree.

class Node:
    def __init__(self, key, value):
        """
        initializes the node
        key: root key 
        value: value assigned to key

        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        """
        key: append key
        value: value assigned to key
       
        """
        if key == self.key:
            return
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Node(key, value)
        else:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Node(key, value)
  

    def get(self, val):
        """
        val: value to search in tree 
        return: the data asociated to that value
        """
        if val == self.key:
            #modify the return
            print(f" Get key: {self.key} , value: {self.value}")
            return self.value
        if val < self.key:
            if self.left:
                return self.left.get(val)
            else:
                return False
        else:
            if self.right:
                return self.right.get(val)
            else:
                return False  


    def print(self):
        """
        print the tree
        """
        space=" "
        #print(f"{50*space} + {self.key}")
        height=tree.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        offset = int((width - 1) / 2)

        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            
            row = self.getNodesAtDepth(depth, [])
            print((' ' * offset) + ''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print('/')

    def height(self, h=0):
        """
        auxiliary function to print the tree
        """
        leftHeight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight, rightHeight)

    def _nodeToChar(self, n, spacing):
        """
        auxiliary function to print the tree
        """
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n) + (' ' * spacing)
    
    def getNodesAtDepth(self, depth, nodes=[]):
        """
        auxiliary function to print the tree
        """
        if depth == 0:
            nodes.append(self.key)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        if self.right:
            self.right.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        return nodes


#add first node
tree=Node("Vahe", 40)

#use insert to add more nodes
tree.insert("Thomas",41)
tree.insert("Anna",32)
tree.insert("Andrew",25)
tree.insert("William",20)
tree.insert("Daniel",54)
tree.insert("Serena",15)

#use the get function to obtain the value asociated
print(tree.get("Vahe"))
print(tree.get("Serena"))

#print tree
tree.print()



