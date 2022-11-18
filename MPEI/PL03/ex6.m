% (a)
%      1   2   3  4  5
T = [ 0.8  0   0 0.3 0
      0.2 0.6  0 0.2 0
      0.3 0.3  1  0  0
       0  0.1  0 0.4 0
       0   0   0 0.1 1];
sum(T);

% (b) - p(1->2)
n = 1:100;
v = [1; 0; 0; 0; 0];
estado2 = zeros(100,1);

for i=1:100
    v=T*v;
    estado2(i) = v(2);
end
figure(1);
plot(n,estado2);
fprintf('alinea b\n');
fprintf('probabilidade de estar no 2: %.10f\n',v(2));
fprintf('\n');

% (c)
%alinea c
v1 = [1;0;0;0;0];
estado3 = zeros(100,1);
estado5 = zeros(100,1);
for i=1:100
    v1=T*v1;
    estado3(i) = v1(4);
end

v2 = [1; 0; 0; 0; 0];

for i=1:100
    v2=T*v2;
    estado5(i) = v2(5);
end
figure(2);
subplot(1,2,1)
plot(n,estado3);
subplot(1,2,2);
plot(n,estado5);
fprintf('alinea c\n');
fprintf('probabilidade de estar no 3: %.10f\n',v1(4));
fprintf('probabilidade de estar no 5: %.10f\n',v2(5));
fprintf('\n');

% (d)
Q = T(1:3,1:3)

% (e)
F = inv(eye(3)-Q)

% (f)
sum(F)

% (g)
R = T(4:5,1:3)
B = R * F

resp_estado3 = B(1,1)
resp_estado5 = B(2,1)

