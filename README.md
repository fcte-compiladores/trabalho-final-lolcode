[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Hppw7Zh2)

# LOLCODE Interpreter in Python

## Integrantes

- Diego Sousa Leite - 221007994 - Turma 3
- João Artur Leles Ferreira Pinheiro - 221031185 - Turma 2
- Pedro Gois Marques Monteiro - 222026386 - Turma 3
- William Bernardo da Silva - 222021933 - Turma 2


## Introdução

Este projeto implementa um interpretador para um subconjunto da linguagem de programação esotérica LOLCODE v1.2. O objetivo é demonstrar os conceitos fundamentais da construção de compiladores, incluindo análise léxica, sintática e semântica.

Nossa abordagem utiliza um interpretador do tipo **tree-walking**. O código fonte em LOLCODE é primeiro transformado em uma sequência de tokens (análise léxica), depois organizado em uma Árvore de Sintaxe Abstrata (AST) que representa a estrutura do programa (análise sintática). Finalmente, o interpretador percorre essa árvore recursivamente para executar o código e realizar verificações semânticas, como o uso de variáveis não declaradas.

**Exemplo de Sintaxe Suportada:**

* **Declaração de Variável e Output:**
    ```lol
    HAI 1.2
    I HAS A GREETING ITZ "Hello, World!"
    VISIBLE GREETING
    KTHXBYE
    ```
    *Semântica: Declara uma variável `GREETING` com o valor "Hello, World!" e a imprime na tela.*

* **Input e Operações Matemáticas:**
    ```lol
    HAI 1.2
    I HAS A NUM1
    I HAS A NUM2
    GIMMEH NUM1
    GIMMEH NUM2
    VISIBLE SUM OF NUM1 AN NUM2
    KTHXBYE
    ```
    *Semântica: Pede ao usuário dois números, os armazena em `NUM1` e `NUM2`, e imprime a soma deles.*

## Instalação

**Requisitos:**
* Python 3.10+
* Gerenciador de pacotes `uv` (ou `pip`)

**Passos:**
1.  Clone o repositório:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```
2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```
3.  Para rodar o interpretador, execute:
    ```bash
    uv run python -m lolcompiler.main examples/fibonacci.lol
    ```

## Exemplos

A pasta `examples/` contém diversos arquivos de exemplo com complexidade crescente:

* `helloworld.lol`: O clássico "Hello, World!".
* `calculator.lol`: Pede dois números e mostra a soma, diferença, etc.
* `fibonacci.lol`: Calcula e exibe os primeiros N números da sequência de Fibonacci (exemplo com laços).
* `factorial_recursive.lol`: Calcula o fatorial de um número usando uma função recursiva (exemplo com funções).

## Referências

* **Especificação Oficial do LOLCODE v1.2:** [Link para a especificação](https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md). Foi a principal referência para a sintaxe e semântica da linguagem.
* **Crafting Interpreters por Robert Nystrom:** [craftinginterpreters.com](https://craftinginterpreters.com/). O livro foi fundamental para entender o padrão de projeto *tree-walking interpreter* e a estruturação geral do código. Nossos módulos `lexer`, `parser` e `interpreter` são fortemente inspirados na abordagem do livro.
* **Documentação da Biblioteca SLY:** [sly.readthedocs.io](https://sly.readthedocs.io/). Utilizamos a biblioteca `sly` para a implementação do lexer e do parser, o que facilitou a definição da gramática e a geração dos tokens.

## Estrutura do Código

O código-fonte está organizado nos seguintes módulos principais dentro da pasta `lolcompiler/`:

* `lexer.py`: Responsável pela **análise léxica**. Contém a classe `LolLexer` que define todos os tokens da nossa linguagem e os converte a partir do código fonte.
* `parser.py`: Responsável pela **análise sintática**. Contém a classe `LolParser` que define a gramática da linguagem e constrói a Árvore de Sintaxe Abstrata (AST). As classes que representam os nós da AST também estão aqui.
* `interpreter.py`: Implementa o interpretador (a fase de **execução** e **análise semântica**). A classe `Interpreter` usa o padrão Visitor para percorrer a AST gerada pelo parser e executar as ações correspondentes. Também mantém uma tabela de símbolos para gerenciar as variáveis.
* `main.py`: O ponto de entrada do programa. Ele orquestra o processo: lê o arquivo `.lol`, passa o conteúdo para o lexer, os tokens para o parser, e a AST resultante para o interpretador.

## Bugs/Limitações/Problemas Conhecidos

* **Tratamento de Erros:** O tratamento de erros é rudimentar. Erros de sintaxe ou semânticos simplesmente encerram o programa com uma mensagem, sem indicar o número da linha ou a coluna.
* **Tipos de Dados:** Apenas os tipos `NUMBR`, `YARN` e `NOOB` são totalmente suportados. Não há suporte para `TROOF` (booleanos) de forma explícita, embora condicionais funcionem com base no valor de outras variáveis.
* **Escopo de Variáveis:** O escopo é global. Não há escopo de bloco ou de função implementado.
* **Melhoria Futura:** Uma melhoria incremental seria adicionar um sistema de recuperação de erros mais robusto no parser, para que ele pudesse reportar múltiplos erros de sintaxe em uma única execução.


python -m lolcompiler.main examples/helloworld.lol
python -m lolcompiler.main examples/variables.lol
python -m lolcompiler.main examples/error.lol