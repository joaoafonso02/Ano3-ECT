% (a)
N = 1e5;
alpha = ['a':'z' 'A':'Z'];

tic
keys = generator(N,6,20,alpha);
fprintf('1a) No keys: %d\n', length(keys));
fprintf('    No unique: %d\n', length(unique(keys)));
fprintf('    Running Time: %f seconds\n', toc);
save 'keys' 'keys'
% salva keys num ficheiro keys.mat

% load keys --> manda as keys para as variáveis outra vez

% (b)
alphaB = ['a':'z'];
tic
probs = load('prob_pt.txt');
keysB = generator(N,6,20,alphaB,probs);
fprintf('1b) No keys: %d\n', length(keysB));
fprintf('    No unique: %d\n', length(unique(keysB)));
fprintf('    Running Time: %f seconds\n', toc);
save 'keysB' 'keysB' 

%  generator  %
function keys = generator(N,imin,imax,vchar,vprob)
    keys = {}
    n = 0; % number of keys that are on cell array
    Nvchar = length(vchar);
    if nargin==5
        cs = cumsum(vprob);
    end
    while n<N
        % key size generator
        tam = randi([imin, imax]);
        % choose chars
        if nargin==4 % equiprováveis
            aux = randi(Nvchar,1,tam); % 1 line
        else
            aux=zeros(1,tam);
            for i=1:tam
                aux(i) = 1+sum(rand()>cs);
            end
        end
        % get chars
        key = vchar(aux);
        
        % if not on cell array adds key 
        if ~ismember(key,keys)
            n = n+1;
            keys{n} = key;
        end
    end
end

function state = crawl(H, first, last, limit)
    state = [first];
    while (1)
        state(end+1) = nextState(H, state(end));
        if (state(end) == last)
            break;
        end
        if  length(state)==limit
            break;
        end
    end
end
function state = nextState(H, currentState)
    probVector = H(:,currentState)'; 
    n = length(probVector);
    state = discrete_rnd(1:n, probVector);
end
function state = discrete_rnd(states, probVector)
    U=rand();
    i = 1 + sum(U > cumsum(probVector));
    state= states(i);
end
