clear all;

xi = 0:7;
p = ones(1,6)/6;
b = [0 cumsum(p) 1];

stairs(xi,b, 'b'),xlabel('x'),ylabel('y(x)')