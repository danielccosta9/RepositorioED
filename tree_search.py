def interative_Tree_search(self, key):
    if(self.raiz == None):
        return None
    vertice = self.raiz
    while(vertice != None and vertice.key != int(key)):
        if(int(key) < vertice.key):
            vertice = vertice.left
        else:
            vertice = vertice.right

    return vertice