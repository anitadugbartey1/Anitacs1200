#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)

def calculate_sizes(v):
    # Your code goes here
    # Base case is a Null Node, return 0
    if not v:
      return 0
    # Recursively calculate the size of the left subtree and right subtree of vertex
    left_size = calculate_sizes(v.left)
    right_size = calculate_sizes(v.right)
    # Calculate the vertex size by add the left size and right size subtree and add one for the current node 
    v.size = 1 + left_size + right_size
    # Return the vertex size with 
    return v.size 
    pass 


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    # Your code goes here 
     # We want to find a descendant w such that t <= w.size <= 2t.
    
    # Base case: if the current node satisfies the size condition
    if t <= v.size <= 2*t:
        return v
    
    # If the current node's size is greater than 2t, search its children
    # If the left child exists and its size is large enough to potentially contain the answer, explore it
    if v.left and v.left.size >= t:
        return FindDescendantOfSize(t, v.left)
    
    # Otherwise, explore the right child (note: right child might still have enough size)
    if v.right:
        return FindDescendantOfSize(t, v.right)
    
    # If no valid descendant is found, return None
    return None
    pass 