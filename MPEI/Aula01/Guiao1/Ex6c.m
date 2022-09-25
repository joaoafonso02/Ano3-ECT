p = 0.3;
n = 5;
N = 10e5;

for k = 0:n
    k;
    resultado(k+1) = sum(sum(rand(5, N) > p) == k)/N;
    stem(sum(lancamentos))
end
