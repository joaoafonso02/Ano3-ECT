# Compiladores

## Run Commands ANTL-4
```SEMPRE QUE ALTERA ALGUMA COISA:
    antlr4-build

Para criar interpretador dependendo do tipo de dados:
    antlr4-visitor Calculator Interpreter Long

Para criar a main:
    antlr4-main -i -v Interpreter

-> Para testar (Pelo menos o ex2_03):
    echo "( 1 + 2 ) / 3 * 10"  | antlr4-run

-> Para testar temos q avaliar a gramatica, no exercicio 4:

    EXP = op, exp, exp

    Ou seja, operador, numero, numero

Para ver tudo em árvore:

    echo "( 1 + 2 ) / 3 * 10"  | antlr4-test -gui
```
