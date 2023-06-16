grammar Dialogue;

program: (stat? '\n')* EOF;

stat: 
    print 
    | assign
    ;

print: 'print' expr

assign: ID ':' expr;

