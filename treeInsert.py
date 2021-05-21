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
