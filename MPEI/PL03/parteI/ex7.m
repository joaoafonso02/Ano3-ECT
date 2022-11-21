% -------------- a -------------- %
h = [0 0   0 0 1/3 0;
     1 0   0 0 1/3 0;
     0 1/2 0 1 0   0;
     0 0   1 0 0   0;
     0 1/2 0 0 0   0;
     0 0   0 0 1/3 0];

% Probabilidade de transição inicial igual para todos
x0 = [1/6; 1/6; 1/6; 1/6; 1/6; 1/6;]; 
x10 = (h^(10-1))*x0;

plot(1:6, x10);
xlabel("Estados");
ylabel("Probabilidades do estado");
hold on;

% -------------- b --------------- %
fprintf("\nAs spider traps são C e D\n");
fprintf("O dead-end é F\n");

% -------------- c --------------- %
h = [0 0   0 0 1/3 1/6;
     1 0   0 0 1/3 1/6;
     0 1/2 0 1 0   1/6;
     0 0   1 0 0   1/6;
     0 1/2 0 0 0   1/6;
     0 0   0 0 1/3 1/6];

% Probabilidade de transição inicial igual para todos
x0 = [1/6; 1/6; 1/6; 1/6; 1/6; 1/6;]; 
x10 = (h^(10-1))*x0;

plot(1:6, x10, "r--");
xlabel("Estados");
ylabel("Probabilidades do estado");

% -------------- d --------------- %
h = [0 0   0 0 1/3 1/6;
     1 0   0 0 1/3 1/6;
     0 1/2 0 1 0   1/6;
     0 0   1 0 0   1/6;
     0 1/2 0 0 0   1/6;
     0 0   0 0 1/3 1/6];

beta = 0.8;
umPorN = ones(6,6);
umPorN = umPorN .* (1/6);
a = (beta * h) + (1-beta)*umPorN;

% Probabilidade de transição inicial igual para todos
x0 = [1/6; 1/6; 1/6; 1/6; 1/6; 1/6;]; 
x10 = (a^(10-1))*x0;

plot(1:6, x10, ":");
xlabel("Estados");
ylabel("Probabilidades do estado");
hold off;

% --------------- e -------------- %
i = 2;
diff = 1;
max_diff = 10^(-4);
rAnterior =(a^0)*x0;

% Enquanto a diferença for menor que o valor máximo
while diff > max_diff
    rAtual = (a^(i-1))*x0;
    diff = max(abs(rAtual - rAnterior));

    i = i + 1;
    rAnterior = rAtual;
end
fprintf("Demorou %d iterações\n", i);
disp(rAtual);
