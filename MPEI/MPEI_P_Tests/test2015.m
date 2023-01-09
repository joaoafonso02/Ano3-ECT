%% exercício 1

% a)
T = [ 0.9   0   0.5
      0.09  1   0.4
      0.01  0   0.1 ]
sum(T);
v = [ 0 0 1]';

% b)
x3 = T^3 * v; 

% c)


%% exercício 2
% a)
H = [  0    1/2     1/3      1/4         0
      1/2    0       0       1/4        1/2                               
      1/2   1/2     1/3      1/4         0
       0     0       0        0         1/2 
       0     0      1/3      1/4         0   ];
N = ones(5,5) ./ 5;
A = 0.8 * H + (1 - 0.8) * N; 

% b)
rank10 = A^10 * N % 1st elem of each row gives C, D, E, F, G
fprintf('Pagerank para C: %d\n',rank10(1))
fprintf('Pagerank para D: %d\n',rank10(2))
fprintf('Pagerank para E: %d\n',rank10(3))
fprintf('Pagerank para F: %d\n',rank10(4))
fprintf('Pagerank para G: %d\n',rank10(5))

%% exercício 3

% a)
%       a   b   c   d   ?   .
T = [  0.7  0.2  0   0   0   0        % a
       0.2  0  0.3  0   0   0        % b
        0  0.6 0.3  0   0   0        % c
       0.1 0.2 0.3 0.1  0   0        % d
        0   0   0  0.4  1   0        % ?
        0   0  0.1 0.5  0   1      ];% .   
% b)
vi = [ 1   0   0   0   0   0 ]'; % 'a'
v10 = T^9 * vi; % 10º (começa no 0)
v15 = T^14 * vi;% 15º

% c)
Q = T(1:4, 1:4);
F = inv(eye(size(Q)) - Q);
n = sum(F);
n(3)
                                    


