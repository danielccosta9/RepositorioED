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