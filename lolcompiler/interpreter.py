from .ast import Number, Yarn, Identifier, VariableDeclaration, Visible, Program, BinaryOp

class Interpreter:
    def __init__(self):
        
        self.variables = {}

    def visit(self, node):
        """
        O método 'visit' é o nosso despachante (dispatcher).
        Ele descobre o tipo do nó e chama o método 'visit_TIPO' correspondente.
        Ex: Se o nó é um 'Number', ele chama 'self.visit_Number(node)'.
        """
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Método chamado caso não haja um método 'visit_TIPO' específico."""
        raise Exception(f'Nenhum método visit_{type(node).__name__} encontrado')

    def visit_Program(self, node):
        """Executa cada statement do programa."""
        for statement in node.statements:
            self.visit(statement)

    def visit_VariableDeclaration(self, node):
        """Processa a declaração de uma variável."""
        value = None
        if node.value:
            value = self.visit(node.value) 
        
        self.variables[node.name] = value

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

    def visit_Identifier(self, node):
        """Busca o valor de uma variável na tabela de símbolos."""
        var_name = node.name
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            # Erro semântico! Variável não foi declarada.
            raise NameError(f"Variável '{var_name}' não foi declarada.")
    
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