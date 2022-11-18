% (a)

T = [0.7 0.2 0.3
     0.2 0.3 0.3
     0.1 0.5 0.4];

sum(T);

% (b)
% P(sol) * P(sol->sol) * P(sol->sol)
p = 1*T(1,1)*T(1,1); % 1*0.7*0.7

fprintf('Alinea (b)\n');
fprintf('Probabilidade de estar sol no 2º e 3º dia: %.3f\n',p);
fprintf('\n');

% (c)
% T * [0.7 0.2 0] / (0.7 + 0.2)
v = [0.7
     0.2
     0  ]

v2 = T*v;
w = v2/(v2(1)+v2(2)); % sol e das nuvens
v(3) = 0;  % probabilidade de chuva
v3 = T * w; 
r = v(1)* (v2(1)+v2(2)) * (v3(1)+v3(2));

fprintf('Alinea (c)\n');
fprintf('Probabilidade de não chover no 2º e 3º dia: %.3f\n',r);
fprintf('\n');

% (d)
v = [1; 0; 0];
count_sol = v(1);
count_nuv = v(2);
count_chuv = v(3);
for i= 2:31
    v = T*v;
    count_sol = count_sol + v(1);
    count_nuv = count_nuv + v(2);
    count_chuv = count_chuv + v(3);
end
fprintf('alinea d\n');
fprintf('sol: %.2f\nnuvens: %.2f\nchuva: %.2f\n',count_sol,count_nuv,count_chuv);
fprintf('\n');

% (e) 

v = [0; 0; 1];
count_sol = v(1);
count_nuv = v(2);
count_chuv = v(3);

for i= 2:31
    v = T*v;
    count_sol = count_sol + v(1);
    count_nuv = count_nuv + v(2);
    count_chuv = count_chuv + v(3);
end

fprintf('Alinea (e)\n');
fprintf('%.2f\nnuvens: %.2f\nchuva: %.2f\n',count_sol,count_nuv,count_chuv);
fprintf('\n');

% (f)

v = [1; 0; 0];
count1 = 0.1*v(1) + 0.3*v(2) + 0.5*v(3);

for i= 2:31
    v = T*v;
    count1 = count1 + 0.1*v(1) + 0.3*v(2) + 0.5*v(3);
end

v = [0; 0; 1];
count2 = 0.1*v(1) + 0.3*v(2) + 0.5*v(3);

for i= 2:31
    v = T*v;
    count2 = count2 + 0.1*v(1) + 0.3*v(2) + 0.5*v(3);
end

fprintf('Alinea (f)\n');
fprintf('Dores reumaticas sol: %.2f\ndores reumaticas chuva: %.2f\n', count1, count2);
fprintf('\n');
