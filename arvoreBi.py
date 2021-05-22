class Nodo:
     
     def __init__(self, chave, right, left):
          self.chave = chave
          self.right = right
          self.left = left

class tree:

    def __init__(self):
          self.raiz = Nodo(None,None,None)
          self.raiz = None


    def tree_remove(self, z):
        if(z.left == None):
            self.tree_transplant(z, z.right)
        elif(z.right == None):
            self.tree_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)

            if(y.pai != z):
                self.tree_transplant(y, y.right)
                y.right = z.right
                y.right.pai = y
            
            self.tree_transplant(z, y)
            y.left = z.left
            y.left.pay = y


    def tree_sucessor(self, vertice):
        
        if(vertice.right != None):
            return self.tree_minimun(vertice = vertice.right)
 
        y = vertice.pai
        while(y != None and vertice == y.right):
            vertice = y
            y = vertice.pai
        return y


    def tree_transplant(self, u, v):
        if(u.pai == None):
            self.raiz = v
        elif(u.pai.left == u):
            u.pai.left = v
        else:
            u.pai.right = v
        
        if(v != None):
            v.pai = u.pai

    def treeInsert(self, z):
        y = None
        x = self.raiz

        while (x != None):
            y = x
            if(z.key < x.key):
                x = x.left
            else:
                x = x.right

        z.pai = y

        if(y == None):
            self.riz = z
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z
        self.count += 1

    
    def interative_tree_search(self, key):
        if(self.raiz == None):
            return None
        vertice = self.raiz
        while(vertice != None and vertice.key != int(key)):
            if(int(key) < vertice.key):
                vertice = vertice.left
            else:
                vertice = vertice.right

        return vertice


    def inorde_tree_walk(self, vertice = None):
        if(self.raiz == None): 
            return
        
        if(verice == None):
            vertice = self.raiz
        
        if(vertice.left != None): 
            self.inorde_tree_walk(vertice = vertice.left)

        print(vertice)

        if(vertice.right != None): 
            self.inorde_tree_walk(vertice = vertice.right)


    def tree_minimum(self, vertice = None):
        if(self.raiz == None): 
            return None
            
        if(vertice == None):
            vertice = self.raiz
        
        while(verice.left != None):
            vertice = vertice.left
        return vertice

    def tree_minimum_recu(self):
        if self.left is None:
            return self
        else:
            return self.left.tree_minimum_recu()

    
    def tree_pre_order(self, vertice):
         if vertice != None:
              print(vertice.item,end=" ")
              self.tree_pre_order(vertice.left)
              self.tree_pre_order(vertice.right)
       
    
    def tree_pos_order(self, vertice):
        if vertice != None:
            self.tree_pos_order(vertice.left)
            self.tree_pos_order(vertice.right)
            print(vertice.item,end=" ")
