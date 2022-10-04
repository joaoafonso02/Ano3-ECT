%Ex2c

dardos = [10:10:100];
alvos = [1e3 1e5];
N = 1e6;

for g = 1:2              % g =1:2 porque vamos fazer 2 graficos
  subplot(2,2,g);      % subplot(2,2,g) porque
  probs = 0*dardos;    % probs = [0,0,0] nr de diferentes instancias de dardos(neste caso 10)
  for i = 1:length(dardos)  %for i=1:10
    probs(i) =  1 - alvoCalc(dardos(i), N, alvos(g)); %prob(i) = 1 - (prob de nunca repetir)
  end

  plot(dardos(1:i),probs(1:i),"r.");    %plot(dardos(1:10),probs(1:10),"r.")
  xlabel('dardos');                     
  ylabel('prob');                       
  title(["alvos=" num2str(alvos(g))]);  
end