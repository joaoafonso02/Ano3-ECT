clear all
%     1   3    5   7    9   Fim
T = [ 0   4/15 0   4/15 0   0 % 1
      1/3 0    1/2 0    2/5 0 % 3
      1/3 4/15 0   4/15 0   0 % 5
      1/3 0    1/2 0    2/5 0 % 7
      0   4/15 0   4/15 0   0 % 9
      0   1/5  0   1/5  1/5 0]%Fim

%sum(T)

fprintf("(c) \n")

state = crawl(T, getrand(), 6)

N = 10e5;
size = 0;
soma = 0;
numC = 0;
for i = 1: N
    x = getrand();
    state = crawl(T, x, 6);
    if isequal([1 2 3 4 5 6],state)
        soma = soma + 1; 
    end
    if state(1) == 1
        size = size + length(state);
        numC = numC +1 ;
    end
    c(:, i)= {state};
end
prob = soma / N
media = size/numC

function [y] = getrand()
    y = ceil(rand(1,1)*4);
    if y == 2
      if rand(1,1)<0.5
          y = 2;
      else 
          y = 5;
      end
    end
end


function [state] = crawl(H, first, last)
     % the sequence of states will be saved in the vector "state"
     % initially, the vector contains only the initial state:
     state = [first];
     % keep moving from state to state until state "last" is reached:
     while (1)
          state(end+1) = nextState(H, state(end));
          if ismember(state(end), last) % verifies if state(end) is absorving
              break;
          end
     end
end

% Returning the next state
% Inputs:
% H - state transition matrix
% currentState - current state
function state = nextState(H, currentState)
     % find the probabilities of reaching all states starting at the current one:
     probVector = H(:,currentState)';  % probVector is a row vector 
     n = length(probVector);  %n is the number of states
     % generate the next state randomly according to probabilities probVector:
     state = discrete_rnd(1:n, probVector);
end

% Generate randomly the next state.
% Inputs:
% states = vector with state values
% probVector = probability vector 
function state = discrete_rnd(states, probVector)
     U=rand();
     i = 1 + sum(U > cumsum(probVector));
     state= states(i);
end