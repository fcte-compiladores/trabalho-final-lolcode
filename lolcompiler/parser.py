from sly import Parser
from .lexer import LolLexer
from .ast import Program, Visible, Number, Yarn, Identifier, VariableDeclaration, BinaryOp

class LolParser(Parser):
    tokens = LolLexer.tokens

    debugfile = 'parser.out'


    @_('HAI NUMBR_F statement_list KTHXBYE',
       'HAI NUMBR_I statement_list KTHXBYE')
    def program(self, p):
        return Program(p.statement_list)

    @_('statement_list statement')
    def statement_list(self, p):
        return p.statement_list + [p.statement]

    @_('empty')
    def statement_list(self, p):
        return []

    @_('visible_statement',
       'var_decl_statement')
    def statement(self, p):
        return p[0]

    @_('VISIBLE expr')
    def visible_statement(self, p):
        return Visible(p.expr)
    
    @_('I_HAS_A IDENTIFIER ITZ expr')
    def var_decl_statement(self, p):
        return VariableDeclaration(name=p.IDENTIFIER, value=p.expr)

    @_('I_HAS_A IDENTIFIER')
    def var_decl_statement(self, p):
        return VariableDeclaration(name=p.IDENTIFIER, value=None)
    
    @_('SUM_OF expr AN expr',
       'DIFF_OF expr AN expr',
       'PRODUKT_OF expr AN expr',
       'QUOSHUNT_OF expr AN expr')
    def expr(self, p):

        return BinaryOp(op=p[0], left=p[1], right=p[3])
    
    @_('YARN')
    def expr(self, p):
        return Yarn(p.YARN)

    @_('NUMBR_I', 'NUMBR_F')
    def expr(self, p):
        return Number(p[0])

    @_('IDENTIFIER')
    def expr(self, p):
        return Identifier(p.IDENTIFIER)
    
    @_('')
    def empty(self, p):
        pass

    def error(self, p):
        if p:
            print(f"Erro de sintaxe no token {p.type}('{p.value}') na linha {p.lineno}")
        else:
            print("Erro de sintaxe no final do arquivo!")