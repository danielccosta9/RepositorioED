def tree_transplant(self, u, v):
    if(u.pai == None):
        self.raiz = v
    elif(u.pai.left == u):
        u.pai.left = v
    else:
        u.pai.right = v
    
    if(v != None):
        v.pai = u.pai