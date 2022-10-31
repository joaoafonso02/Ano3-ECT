p = 0.3;
n = 5;
N = 10e5;

pecas = sum(rand(5, N) < p);

for k = 0 : n
    k;

    resultado(k+1) = sum(pecas == k)/N;
    
    % 
end
histogram(pecas)