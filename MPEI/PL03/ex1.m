clear all
% 1 aluno - 2 aulas às 9h na 4ª e 6ª
% presente na anterior --> p("ir à aula")=0,7
% faltou na anterior --> p("ir à aula")=0,8

% (a)
% se está presente na 4ª qual a prob de estar presente na próxima 4ª

%1 - n ir à aula
%2 - ir à aula

T = [0.2 0.3    % soma das colunas = 1
     0.8 0.7];

sum(T);

x = [0
     1]; % estar presente na 1ª e nao estar na 2ª

% ir na prox. aula
x1 = T * x;
% duas aulas depois
x2 = T^2 * x;

fprintf("a: %f\n", x2(2))

% (b)
x = [1
     0]; % n estar presente na 1ª e estar na 2ª

x2 = T^2 * x;
fprintf("b: %f\n", x2(2))

% (c)
x = [0
     1];

x2 = T^(30-1)*x;x
fprintf("c: %f\n", x2(2))



