function [res] = alvoCalc(dardos,N,alvos)
  %m -> numero total de alvos
  %n -> numero de dardos
  %N -> numero de experiencias

  matrix = randi([1,alvos],dardos,N);
  %Vamos gerar uma matriz com 20 linhas e 1e5 colunas
  %Cada coluna corresponde a uma repeticao da experiencia
  %Cada linha corresponde a um lancamento do dardo (indicando
  %em qual dos alvos, de 1 a 100, aterrou

  sucesso = 0; %Contador de sucessos
  for col=1:N
    if length(unique(matrix(:,col)))==dardos %Percorrendo alvos coluna a coluna, consideramos que houve
        sucesso=sucesso+1;                   %sucesso se o numero de elementos unicos daquela coluna
    end                            %for igual a 20 (todos os alvos sao diferentes
  end                            %Notar que unique() da nos um array com os elementos nao repetidos de cada coluna de alvos

  res = sucesso/N;
end