%%Ex 3

%a)
  T = [ 0.7 0.2 0.0 0.0 0.0 0.0 ;
        0.2 0.0 0.3 0.0 0.0 0.0 ;
        0.0 0.6 0.3 0.0 0.0 0.0 ;
        0.1 0.2 0.3 0.1 0.0 0.0 ;
        0.0 0.0 0.0 0.4 1.0 0.0 ;
        0.0 0.0 0.1 0.5 0.0 1.0 ];
        
%b)
  x0 = [1 0 0 0 0 0]';
  
  x9 = T^9 * x0;
  
  display("C:");
  x9(1)
  
  x14 = T^14 * x0;
  display("D:");
  x14(2)
  
%c)
  Q = T(1:4,1:4);
  
  F = inv(eye(size(Q))-Q)
  
  comp = sum(F);
  
  comp(1)