from .ast import Number, Yarn, Identifier, VariableDeclaration, Visible, Program, BinaryOp, FunctionDeclaration, Return, FunctionCall

class ReturnSignal(Exception):
    """Exceção customizada usada para sinalizar um 'return' de função."""
    def __init__(self, value):
        self.value = value

class Environment:
    """Gerencia os escopos de variáveis (tabelas de símbolos)."""
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent # Referência ao escopo pai (ex: global)

    def get(self, name):
        """Busca uma variável no escopo atual ou nos pais."""
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise NameError(f"Variável '{name}' não foi declarada.")

    def set(self, name, value):
        """Define uma variável no escopo atual."""
        self.variables[name] = value

class Interpreter:
    def __init__(self):
        self.environment = Environment()
        self.functions = {}

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Nenhum método visit_{type(node).__name__} encontrado')

    def visit_Program(self, node):
        for statement in node.statements:
            if isinstance(statement, FunctionDeclaration):
                self.visit(statement)
        
        for statement in node.statements:
            if not isinstance(statement, FunctionDeclaration):
                self.visit(statement)

    def visit_FunctionDeclaration(self, node):
        self.functions[node.name] = node

    def visit_VariableDeclaration(self, node):
        value = None
        if node.value:
            value = self.visit(node.value)
        self.environment.set(node.name, value)

    def visit_Identifier(self, node):
        return self.environment.get(node.name)
        
    def visit_FunctionCall(self, node):
        func_name = node.name
        if func_name not in self.functions:
            raise NameError(f"Função '{func_name}' não foi definida.")

        func_decl = self.functions[func_name]

        if len(node.args) != len(func_decl.params):
            raise TypeError(f"Função '{func_name}' espera {len(func_decl.params)} argumentos, mas recebeu {len(node.args)}.")

        arg_values = [self.visit(arg) for arg in node.args]

        func_env = Environment(parent=self.environment)

        for param_name, arg_value in zip(func_decl.params, arg_values):
            func_env.set(param_name, arg_value)
        
        original_env = self.environment
        self.environment = func_env

        return_value = None
        try:
            for statement in func_decl.body:
                self.visit(statement)
        except ReturnSignal as ret:
            return_value = ret.value
        finally:
            self.environment = original_env

        return return_value

    def visit_Return(self, node):
        value = self.visit(node.value)
        raise ReturnSignal(value)

    def visit_Visible(self, node):
        """Processa o comando VISIBLE."""
        value = self.visit(node.expression)
        print(value)

    def visit_Number(self, node):
        """Retorna o valor numérico bruto."""
        return node.value

    def visit_Yarn(self, node):
        """Retorna o valor da string bruta."""
        return node.value


    def visit_BinaryOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)

        if not isinstance(left_val, (int, float)) or not isinstance(right_val, (int, float)):
            raise TypeError("Operações matemáticas só podem ser feitas com NUMBRs.")

        if node.op == 'SUM OF':
            return left_val + right_val
        elif node.op == 'DIFF OF':
            return left_val - right_val
        elif node.op == 'PRODUKT OF':
            return left_val * right_val
        elif node.op == 'QUOSHUNT OF':
            if right_val == 0:
                raise ZeroDivisionError("Divisão por zero não permitida.")
            return left_val / right_val