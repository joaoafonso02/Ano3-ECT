% Ex4 
% nº n de pessoas

N = 1e5;
p = 0.9;

clear res

for pessoas = 2 : 366 %com 366 pessoas é grantido ter duas pessoas a ter a mesma data de nascimento
    a = randi(365, pessoas, N);
    for i = 1:N
        res(i) = length(unique(a(:, i))) < pessoas;
    end
    prob = sum(res)/N;
    if (prob > p)
        pessoas
        break
    end
end