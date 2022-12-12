fid = fopen('wordlist-preao-20201103.txt','r');
dicionario = textscan(fid, '%s');
fclose(fid);
dicionario = dicionario{1,1};

%exercicio 1
%criar bloom filter para um conjunto de 1000 palavras diferentes
n = 8000;
m = 1000;
%k=6 é o valor ótimo
k=3;
bloomFilter = inicFiltroBloom(n);
for i=1:m
   bloomFilter = addElem(dicionario{i},bloomFilter,n,k);
end
contador = 0;
for i=1:m
   bool = isElem(dicionario{i},bloomFilter,n,k);
   if bool==0
       contador=contador +1;
   end
end

fprintf('Num falsos negativos = %d\n',contador);

contador =0;
m2=10000;
for i=m+1:m+m2
   bool = isElem(dicionario{i},bloomFilter,n,k);
   if bool==1
       contador=contador +1;
   end
end

fprintf('Percentagem de falsos positivos = %.2f%%\n',(contador/m2)*100);

probFalsosPositivosTeorica = (1-exp(-k*m/n))^k;
fprintf('Percentagem de falsos positivos teórica = %.2f%%\n',probFalsosPositivosTeorica*100);

%inicializar filtro
function fb = inicFiltroBloom(n)
    fb = zeros(1,n);
end

%adicionar elem
function fb = addElem(string,fb,n,k)
    for i=1:k
        string=[string num2str(i)];
        hash = DJB31MA(string,127);
        hash = mod(hash,n)+1;
        fb(hash) = 1;
    end
end

%verificar elem se existe
function bool = isElem(e,fb,n,k)
    bool = 1;
    for i=1:k
        e = [e num2str(i)];
        hash = DJB31MA(e,127);
        hash = mod(hash,n)+1;
        if fb(hash)==0
            bool = 0;
            break;
        end
    end
end