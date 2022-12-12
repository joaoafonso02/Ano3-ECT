load keys
Nchaves = length(keys);
Ntabela = 5e5;
Ntabela2 = 1e6;
Ntabela3 = 2e6;
valores = zeros(1,Nchaves);
tabela = zeros(1,Ntabela3);
colisoes = 0;
tic
%para função string2hash tamanho 5e5
for i=1:Nchaves
    
    %hash=string2hash(keys{i});
    %hash=mod(hash,Ntabela)+1;
    
    %hash=string2hash(keys{i},'sdbm');
    %hash=mod(hash,Ntabela)+1;
    
    %hash=hashstring(keys{i},Ntabela3)+1;
    
    hash=DJB31MA(keys{i},127);
    hash=mod(hash,Ntabela)+1; %converter valor entre 0(+1) e Ntabela-1(+1)
    
    valores(i)=hash;
    if tabela(hash)>0
        colisoes=colisoes+1;
    end
    %contar num de vezes que posiçao na tabela foi atribuida
    tabela(hash)=tabela(hash) + 1;
end
tempo = toc;

%exercicio 3
h=valores/Ntabela3;
histogram(valores,100)
fprintf('Momento 2: medido- %f teórico- %f\n',mean(h.^2),1/(2+1));
fprintf('Momento 5: medido- %f teórico- %f\n',mean(h.^5),1/(5+1));
fprintf('Momento 10: medido- %f teórico- %f\n',mean(h.^10),1/(10+1));
fprintf('Num de colisões: %d\n',colisoes);
fprintf('Num de atribuições: %d\n',max(tabela));
fprintf('Tempo de execução: %f\n',tempo);

%valores e histogramas semelhantes das 4 funçoes uniformidade semalhante em todas
%comparar colisoes e atribuiçoes a pior é a hashstring as outras sao equivalentes
%djb31ma mais rápida

%operações do bitshift matlab na funçao hashstring sao pouco eficientes 

%concluoes parecidas para keysB (djb31ma é um bocadinho pior)




