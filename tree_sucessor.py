def tree_sucessor(self, vertice):
    # Caso 1
    if(vertice.right != None):
        return self.tree_minimun(vertice = vertice.right)

    # Caso 2
    y = vertice.pai
    while(y != None and vertice == y.right):
        vertice = y
        y = vertice.pai
    return y