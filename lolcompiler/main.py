import sys
from .lexer import LolLexer
from .parser import LolParser 

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

        print("--- Código Fonte ---")
        print(code)
        
        ast = parser.parse(lexer.tokenize(code))

        print("\n--- Árvore de Sintaxe Abstrata (AST) ---")
        print(ast)
        print("----------------------------------------")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{file_path}'")
        sys.exit(1)

if __name__ == "__main__":
    main()