%%Ex 1

%a)
  T = zeros(3,3);
  T(1,1) = 1-0.09-0.01;
  T(1,2) = 1-0.4-0.1;
  T(2,1) = 0.09;
  T(2,2) = 0.4;
  T(3,1) = 0.01;
  T(3,2) = 0.1;
  
  T(:,3) = T(:,2)
  
  v = [0 0 1]'
%b)
  %1o pacote = x0 = v, logo
  %4o pacote = x3
  
  x3 = T^3*v

%c)
  
  xn = v;
  i = 1;
  graphProb = [];
  
  while 1
    xOld = xn;
    xn = T^i*v;
    
    if(max(abs(xn-xOld))<1e-3)
      break;
    endif
    
    graphProb = [graphProb xn];
    plot(graphProb');
    drawnow();
    
    i++;
  endwhile
  
  xlabel("Trans");
  ylabel("Prob");
  xn(3)
  xn(2)+xn(3)
  
  
