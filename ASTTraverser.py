class ASTTraverser(object):
    def __init__(self):
        pass


    ##############################
    ## Methods to visit the AST ##
    ##############################
    def visit(self, tree):
        print("Visitor")
        method = getattr(self, tree.head, None)
        # print("Visit for {} will call {}".format(tree.head, method))
        if method:
            return method(tree)
        else:
            print("Method {} is not defined by the class".format(method))

    def start(self, tree):
        print("Start*- {}".format(tree))
        # la regla start solo puede tener un hijo (segun la gramatica) y estará
        # en tree.tail[0]
        le = tree.tail[0]
        self.visit(le)
    
    def logicalexpression(self, tree):
        print("Logical expression {}".format(tree))
        print(len(tree.tail))
        if len(tree.tail) == 1:
            self.visit(tree.tail[0])
        else:
            print("No implementado")
    
    def parenle(self, tree):
        print("parenle {}".format(tree))
        print(len(tree.tail))

   