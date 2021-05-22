def Tree_minimum(self, vertice = None):
    if(self.raiz == None): #arvore vazia
        return None

    if(vertice == None):
        vertice = self.raiz
    
    while(verice.left != None):
        vertice = vertice.left
    return vertice
