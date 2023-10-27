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
        program = tree.tail[0]
        #self.visit(program)

   