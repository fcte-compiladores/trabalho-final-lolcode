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