class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class TreeHeap:
    __slots__ = '_root', '_last', '_size'

    #-------------------- nonpublic
    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'
        def __init__(self, element, left, right, parent):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent
    
    def _swap(self, node1, node2):
        """Swap the elements at indices i and j of array."""
        # IMPLEMENT HERE
        subnode = node1._element
        node1._element = node2._element
        node2._element = subnode

        
    def _upheap(self, node):
        # IMPLEMENT HERE
        if node._parent != None:
            pnode = node._parent._element
            cnode = node._element
            
            if pnode > cnode:
                self._swap((node._parent), node)
                self._upheap(node._parent)

    def _downheap(self, node):
        # IMPLEMENT HERE
        if node._left != None:
            if node._right != None:
                pnode = node._element
                lnode = node._left._element
                rnode = node._right._element
                snode = node._left
                if lnode > rnode:
                    snode = node._right
                if pnode > snode._element:
                    self._swap(node, snode)
                    self._downheap(snode)
            else:
                pnode = node._element
                snode = node._left
                if pnode > snode._element:
                    self._swap(node, snode)
                    self._downheap(snode)

    #-------------------- public
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._root = None
        self._last = None
        self._size = 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def add(self, key):
        """Add a key to the priority queue."""
        # IMPLEMENT HERE
        node = self._Node(element = key, left = None, right = None, parent = None)

        if self._root == None:
            self._root = node
            self._last = node
            self._size += 1
        else:
            preroot = self._root
            proot = self._root
            subroot = self._root
            self._last = None
            while self._last == None:
                if proot._left == None:
                    node._parent = proot
                    proot._left = node
                    self._last = node
                    self._size += 1
                    self._upheap(self._last)
                elif proot._right == None:
                    node._parent = proot
                    proot._right = node
                    self._last = node
                    self._size += 1
                    self._upheap(self._last)
                else:
                    if preroot != proot:
                        if proot == preroot._right:
                            proot = subroot._left
                            preroot = subroot
                        else:
                            subroot = preroot._left
                            proot = preroot._right
                    else:
                        proot = proot._left


    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap is empty')
        return self._root._element

    
    def remove_min(self):
        """Remove and return the minimum key.
        Raise Empty exception if empty.
        """
        # IMPLEMENT HERE
        if self.is_empty():
            raise Empty('Heap is empty')
        
        elif self._size == 1:
            ans = self._root._element
            self._root = None
            self._size -= 1
            return ans
        
        elif self._size == 2:            
            ans = self._root._element
            self._root._element = self._last._element
            self._root._left = None
            self._size -= 1
            return ans
        

        else:
            self._swap(self._root, self._last)
            ans = self._last._element
            sparent = self._last._parent
            #afdsf
            rmans = self._last
            if sparent._right != None:
                self._last = sparent._left
            else:
                while sparent != sparent._parent._right:
                    if sparent._parent == self._root:
                        sparent = self._root
                        break
                    else:
                        sparent = sparent._parent
                if sparent != self._root:
                    sparent = sparent._parent._left
                while sparent._right != None:
                    if sparent._right == None:
                        self._last = sparent._left
                        sparent = sparent._left
                    else:
                        self._last = sparent._right
                        sparent = sparent._right

            if rmans == rmans._parent._right:
                rmans._parent._right = None
            elif rmans == rmans._parent._left:
                rmans._parent._left = None
            self._size -= 1

            # sorting, downheap
            self._downheap(self._root)
            return ans

    def display(self):
        self._display(self._root, 0)

    def _display(self, node, depth):
        if node == None:
            return

        if node._right != None:
            self._display(node._right, depth+1)
        label = ''
        if node == self._root:
            label += '  <- root'
        if node == self._last:
            label += '  <- last'
        print(f'{"    "*depth}* {node._element}{label}')
        if node._left != None:
            self._display(node._left, depth+1)