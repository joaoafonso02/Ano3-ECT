p = 0.5;
f = 2;
rapaz = 1;
N = 1e5;

filhos = rand(f,N) > p;
res = sum(filhos) >= rapaz;
prob = sum(res) / N

%fprintf("%f", prob)

