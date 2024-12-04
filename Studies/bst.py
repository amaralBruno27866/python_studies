class BST:
  class Node:
    def __init__(self, data=None, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

  def __init__(self):
    self.root = None

  def insert(self, data):
    inserted = False
    if self.root is None:
      self.root = BST.Node(data)
    else:
      curr = self.root
      while not inserted:
        if data < curr.data:
          if curr.left is None:
            curr.left = BST.Node(data)
            inserted = True
          else:
            curr = curr.left
        else:
          if curr.right is None:
            curr.right = BST.Node(data)
            inserted = True
          else:
            curr = curr.right
    return inserted

  def search(self, data):
    curr = self.root

    while curr is not None:
      if data < curr.data:
        curr = curr.left
      elif data > curr.data:
        curr = curr.right
      else:
        return curr
    return None
  
  def delete(self, data):
    self.root = self._delete_rec(self.root, data)

  def _delete_rec(self, node, data):
    if node is None:
      return node
    
    if data < node.data:
      node.left = self._delete_rec(node.left, data)
    elif data > node.data:
      node.right = self._delete_rec(node.right, data)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      
      temp = self._min_value_node(node.right)
      node.data = temp.data
      node.rigth = self._delete_rec(node.right, temp.data)

    return node
  
  def _min_value_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current
  
  def update(self, old_data, new_data):
    if self.delete(old_data):
      self.insert(new_data)
  
  def inorder_print(self, subtree):
    if subtree is not None:
      self.inorder_print(subtree.left)
      print(subtree.data, end = " ")
      self.inorder_print(subtree.right)

  def pre_order_print(self, subtree):
    if subtree is not None:
      print(subtree.data, end = " ")
      self.pre_order_print(subtree.left)
      self.pre_order_print(subtree.right)

  def post_order_print(self, subtree):
    if subtree is not None:
      self.post_order_print(subtree.left)
      self.post_order_print(subtree.right)
      print(subtree.data, end=" ")

  def breadthfirst_print(self, subtree):
    if subtree is not None:
      queue = []
      queue.append(subtree)
      while len(queue) > 0:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)

  def print_between(self, subtree, min_val, max_val):
      if subtree is not None:
        if min_val < subtree.data:
          self.print_between(subtree.left, min_val, max_val)
        if min_val <= subtree.data <= max_val:
          print(subtree.data, end=" ")
        if max_val > subtree.data:
          self.print_between(subtree.right, min_val, max_val)

  def height(self, subtree):
      if subtree is None:
        return -1
      else:
        left_height = self.height(subtree.left)
        right_height = self.height(subtree.right)
        return 1 + max(left_height, right_height)
      
  def inorder_successor(self, value):
    current = self.search(value)
    if current is None:
      return None

    if current.right is not None:
      return self._min_value_node(current.right)

    successor = None
    ancestor = self.root
    while ancestor != current:
      if current.data < ancestor.data:
        successor = ancestor
        ancestor = ancestor.left
      else:
        ancestor = ancestor.right

    return successor

# Exemplo de uso
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    print("Inorder:")
    bst.inorder_print(bst.root)
    print("\nPreorder:")
    bst.pre_order_print(bst.root)
    print("\nPostorder:")
    bst.post_order_print(bst.root)
    print("\nBreadth-first:")
    bst.breadthfirst_print(bst.root)

    print("\n\nDeleting 10")
    bst.delete(10)
    print("Inorder after deletion:")
    bst.inorder_print(bst.root)

    print("\n\nUpdating 5 to 6")
    bst.update(5, 6)
    print("Inorder after update:")
    bst.inorder_print(bst.root)

    print("\n\nValues between 6 and 15:")
    bst.print_between(bst.root, 6, 15)

    print("\n\nHeight of the tree:")
    print(bst.height(bst.root))

    print("\n\nInorder Successor of 6:")
    successor = bst.inorder_successor(6)
    if successor:
        print(successor.data)
    else:
        print("No successor found")