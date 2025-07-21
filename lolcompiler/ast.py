class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program(statements={self.statements})"

class Visible:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Visible(expression={self.expression})"

class VariableDeclaration:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value 
    def __repr__(self):
        return f"VarDecl(name='{self.name}', value={self.value})"

class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class Yarn:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Yarn('{self.value}')"

class Identifier:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier('{self.name}')"
    
class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp(op='{self.op}', left={self.left}, right={self.right})"
    
class FunctionDeclaration:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f"FuncDecl(name='{self.name}', params={self.params}, body={self.body})"

class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"FuncCall(name='{self.name}', args={self.args})"

class Return:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Return(value={self.value})"