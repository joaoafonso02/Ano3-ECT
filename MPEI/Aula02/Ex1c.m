fam = rand(2, 1e5) < 0.5;

no_filhos = sum(fam);

pelo_menos_um_filho_rapaz = no_filhos >= 1;

A = no_filhos == 2;
B = pelo_menos_um_filho_rapaz;

AB = A & B;

P_A_dado_B = sum(AB) / sum(B)