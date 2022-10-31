p = 0.3;
k = 2;
n = 5;
N = 10e5;

lancamentos = rand(n, N) > p;
sucessos= sum(lancamentos)>= k;
prob= sum(sucessos)/N

