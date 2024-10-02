class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int

    def __init__(self, debugger=None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 0  # Initialize size to 0 when key is None
        self.debugger = debugger

    @property
    def size(self):
        return self._size
       
    # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger=None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1 if self.key is not None else 0  # Only count if key exists
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        if self.key is None:
            return None  # Empty tree or subtree

        left_size = self.left.size if self.left else 0

        if ind == left_size:
            return self
        elif ind < left_size:
            if self.left:
                return self.left.select(ind)
            else:
                return None
        else:
            if self.right:
                return self.right.select(ind - left_size - 1)
            else:
                return None

    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self.key is None:
            return None
        elif self.key == key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif key < self.key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        # Only update sizes if the node was actually inserted
        self.calculate_sizes()
        return self

    
    ####### Part b #######
    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == "L":
            child = self.left
        else:  # child_side == "R"
            child = self.right

        if not child:
            raise AttributeError(f"No child on the {child_side} side to rotate.")

        if direction == "L":
            new_child = child.right
            if not new_child:
                raise AttributeError("Cannot perform left rotation; right child is None.")
            child.right = new_child.left
            new_child.left = child
            if child_side == "L":
                self.left = new_child
            else:  # child_side == "R"
                self.right = new_child
        elif direction == "R":
            new_child = child.left
            if not new_child:
                raise AttributeError("Cannot perform right rotation; left child is None.")
            child.left = new_child.right
            new_child.right = child
            if child_side == "L":
                self.left = new_child
            else:  # child_side == "R"
                self.right = new_child
        else:
            raise ValueError("Invalid direction. Use 'L' for left or 'R' for right.")

        self.calculate_sizes()  # Update sizes after rotation
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.print_bst()
        return self
