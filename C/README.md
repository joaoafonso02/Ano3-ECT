# Compiladores

## Run Commands ANTL-4

Any changes:
```bash
    antlr4-build
```

Create Visitor:
```bash
    antlr4-visitor Calculator Interpreter Long
```

Create Main:
```bash
    antlr4-main -i -v Interpreter
```

Test (ex2_03):
```bash
    echo "( 1 + 2 ) / 3 * 10"  | antlr4-run
```

-> Para testar temos q avaliar a gramatica, no exercicio 4:

    EXP = op, exp, exp

    Ou seja, operador, numero, numero

Para ver tudo em árvore:
```bash
    echo "( 1 + 2 ) / 3 * 10"  | antlr4-test -gui
```
