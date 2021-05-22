def inorde_tree_walk(self, vertice = None):
    if(self.raiz == None): #arvore vazia
        return
    
    if(verice == None): #Por padrao comeca pela raiz
        vertice = self.raiz
    
    if(vertice.left != None): #Decomposicao
        self.inorde_tree_walk(vertice = vertice.left)

    print(vertice)

    if(vertice.right != None): #Decomposicao
        self.inorde_tree_walk(vertice = vertice.right)