# lolcompiler/parser.py

from sly import Parser
from .lexer import LolLexer
from .ast import (Program, Visible, Number, Yarn, Identifier, VariableDeclaration, 
                  BinaryOp, FunctionDeclaration, FunctionCall, Return)

class LolParser(Parser):
    tokens = LolLexer.tokens
    debugfile = 'parser.out'

    @_('HAI NUMBR_F top_level_list KTHXBYE', 'HAI NUMBR_I top_level_list KTHXBYE')
    def program(self, p): return Program(p.top_level_list)

    @_('top_level_list top_level_statement')
    def top_level_list(self, p): return p.top_level_list + [p[1]]
    @_('empty')
    def top_level_list(self, p): return []

    @_('statement', 'func_decl')
    def top_level_statement(self, p): return p[0]

    @_('HOW_DUZ_I IDENTIFIER params statement_list IF_U_SAY_SO')
    def func_decl(self, p): return FunctionDeclaration(name=p.IDENTIFIER, params=p.params, body=p.statement_list)
    @_('YR IDENTIFIER param_tail')
    def params(self, p): return [p.IDENTIFIER] + p.param_tail
    @_('param_tail AN YR IDENTIFIER')
    def param_tail(self, p): return p.param_tail + [p.IDENTIFIER]
    @_('empty')
    def params(self, p): return []
    @_('empty')
    def param_tail(self, p): return []

    @_('statement_list statement')
    def statement_list(self, p): return p.statement_list + [p.statement]
    @_('empty')
    def statement_list(self, p): return []

    @_('var_decl', 'visible_statement', 'return_statement', 'function_call')
    def statement(self, p): return p[0]

    @_('VISIBLE expr')
    def visible_statement(self, p): return Visible(p.expr)
    @_('I_HAS_A IDENTIFIER ITZ expr')
    def var_decl(self, p): return VariableDeclaration(name=p.IDENTIFIER, value=p.expr)
    @_('I_HAS_A IDENTIFIER')
    def var_decl(self, p): return VariableDeclaration(name=p.IDENTIFIER, value=None)
    @_('FOUND_YR expr')
    def return_statement(self, p): return Return(p.expr)

    @_('function_call')
    def expr(self, p): return p.function_call
    
    @_('SUM_OF expr AN expr', 'DIFF_OF expr AN expr', 'PRODUKT_OF expr AN expr', 'QUOSHUNT_OF expr AN expr')
    def expr(self, p): return BinaryOp(op=p[0], left=p[1], right=p[3])
    
    @_('IDENTIFIER nonempty_arg_list')
    def function_call(self, p):
        return FunctionCall(name=p.IDENTIFIER, args=p.nonempty_arg_list)
    
    @_('expr')
    def nonempty_arg_list(self, p):
        return [p.expr]
    
    @_('nonempty_arg_list expr')
    def nonempty_arg_list(self, p):
        p.nonempty_arg_list.append(p.expr)
        return p.nonempty_arg_list

    @_('YARN')
    def expr(self, p): return Yarn(p.YARN)
    @_('NUMBR_I', 'NUMBR_F')
    def expr(self, p): return Number(p[0])
    @_('IDENTIFIER')
    def expr(self, p): return Identifier(p.IDENTIFIER)
    
    @_('')
    def empty(self, p): pass

    def error(self, p):
        if p: print(f"Erro de sintaxe no token {p.type}('{p.value}') na linha {p.lineno}")
        else: print("Erro de sintaxe no final do arquivo!")