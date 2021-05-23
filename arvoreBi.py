#Infelizmente nao consegui concluir com exeto esta atividade, espero que compreenda e entenda o meu esforco.

class Nodo:
     
     def __init__(self, key):
          self.key = key
          self.right = None
          self.left = None
          self.pai = None


class Tree:

    def __init__(self):
          self.raiz = Nodo(None)
          self.raiz = None

    def treeInsert(self, key, nodo = None):
        
        if nodo is None:
            nodo = self.raiz
        if self.raiz is None:
            self.raiz = Nodo(key)
        else:
            if key <= nodo.key:
                if nodo.left is None:
                    nodo.left = Nodo(key)
                else:
                    return self.TreeInsert(key, nodo = nodo.left)
            else:
                if nodo.right is None:
                    nodo.right = Nodo(key)
                else:
                    return self.TreeInsert(key, nodo=nodo.right)



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

    def decrescente_tree_walk(self, vertice = None): 

        if (self.raiz == None):
            return

        if (vertice == None):
            vertice = self.raiz

        if (vertice.right != None):
            self.decrescente_tree_walk(vertice = vertice.right)

        print(vertice)

        if (vertice.left != None):
            self.decrescente_tree_walk(vertice = vertice.left)
        
        return vertice


    def inorde_tree_walk(self, vertice = None):

        if (self.raiz == None):
            return

        if (vertice == None): 
            vertice = self.raiz

        if (vertice.left != None):
            self.inorder_tree_walk(vertice = vertice.left)
        print(vertice) 
    
        if (vertice.right != None):
            self.inorder_tree_walk(vertice = vertice.right)


    def tree_minimum(self, vertice = None):
        if(self.raiz == None): 
            return None
            
        if(vertice == None):
            vertice = self.raiz
        
        while(vertice.left != None):
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
            self.tree_pos_order(vertice.right)
            self.tree_pos_order(vertice.left)
            print(vertice.item,end=" ")

arvore = Tree()
arvore.treeInsert(100)
arvore.treeInsert(172)
arvore.treeInsert(50)
arvore.tree_minimum()
arvore.decrescente_tree_walk()