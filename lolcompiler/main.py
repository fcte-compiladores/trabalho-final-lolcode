# lolcompiler/main.py

import sys
from .lexer import LolLexer
from .parser import LolParser
from .interpreter import Interpreter 

def main():
    if len(sys.argv) < 2:
        print("Uso: python -m lolcompiler.main <caminho_para_o_arquivo.lol>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        lexer = LolLexer()
        parser = LolParser()
        
        ast = parser.parse(lexer.tokenize(code))
        
        if ast:
            interpreter = Interpreter()
            interpreter.visit(ast)

    except (FileNotFoundError, NameError, TypeError, ZeroDivisionError) as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()