function[y1] = Ex4(p,n,k,N)
    lancamentos = rand(n,N) > p;
    stem(sum(lancamentos))
    sucessos = sum(lancamentos)==k; 
    
    y1 = sum(sucessos)/N;

end