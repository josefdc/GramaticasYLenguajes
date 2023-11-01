class ASTTraverser(object):
    def __init__(self):
        pass


    ##############################
    ## Methods to visit the AST ##
    ##############################
    def visit(self, tree):
        if isinstance(tree, str):
            # Si es una hoja (string), devuelve su valor.
            return self.handle_terminal(tree)

        method = getattr(self, tree.head, None)
        if method:
            return method(tree)
        else:
            print(f"Method '{tree.head}' is not defined by the class")

    def start(self, tree):
        print("Start*->> {}".format(tree))
        # la regla start solo puede tener un hijo (segun la gramatica) y estará
        # en tree.tail[0]
        le = tree.tail[0]
        return self.visit(le)
    
    def logicalexpression(self, tree):
        print("Logical expression>> {}".format(tree))
        if len(tree.tail) == 1:
            return self.visit(tree.tail[0])
        else:
            print("ENTRO AQUI")
            

    def TRUE(self, tree):
        return True

    def FALSE(self, tree):
        return False

    def parenle(self, tree):
        print("parenle>> {}".format(tree))
        if len(tree.tail) == 3:
            return self.visit(tree.tail[1])
        else:
            print("No implementado")
    
    def negation(self, tree):
        print("negation>> {}".format(tree))
        if len(tree.tail) == 2:
            return not self.visit(tree.tail[1])
        else:
            print("No implementado")

    def conj(self, tree):
        print("Conjunction>> {}".format(tree))
        left = self.visit(tree.tail[0])
        right = self.visit(tree.tail[2])
        return left and right


    def disyu(self, tree):
        print("Disjunction>> {}".format(tree))
        left = self.visit(tree.tail[0])
        right = self.visit(tree.tail[2])
        return left or right
    

    def implication(self, tree):
        print("Implication>> {}".format(tree))
        left = self.visit(tree.tail[0])
        right = self.visit(tree.tail[2])
        return (not left) or right
    
    def dimplication(self, tree):
        print("Dimplication>> {}".format(tree))
        left = self.visit(tree.tail[0])
        right = self.visit(tree.tail[2])
        return (left and right) or (not left and not right)

   
    def handle_terminal(self, token):
        print("Terminal:", token)
        # Aquí puedes manejar los valores terminales directamente.
        # Puedes realizar acciones específicas según el tipo del terminal (por ejemplo, 'TRUE' o 'FALSE').
        if token == 'true':
            return True
        elif token == 'false':
            return False
        else:
            return token


   