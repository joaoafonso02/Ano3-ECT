%% save 
dic = readcell('films.txt', 'Delimiter','\t');

u_data = load('u.data'); % loads file
u = u_data(1:end,1:2);
eval = u_data(1:end,2); % get movies evaluation
clear u_data;


users = unique(u(:,1)); % get users id
No = length(users); % numb of users
save 'noUsers.mat' No

Set = cell(No,1); % use cells
for n = 1:No                
    ind = find(u(:,1) == users(n));
    Set{n} = [Set{n} u(ind,2)];
end

% saves set and dic
save 'users.mat' Set
save 'movies.mat' dic

%% Counting bloom filter
for i=1:length(users)
    vec{i,1} = u(i,2);
end

n =length(vec) * 8;
m = length(vec);
k = 3;

BF = init(n);

for i = 1:m
    BF = insert(vec{i}, BF, k);
end

save 'BF.mat' BF
%% MinHashes

K = 100;  % number of  funções de dispersão’
MinHashValue = inf(No,K);
for i = 1: No
    group = Set{i};
    for j = 1:length(group)
        chave = char(group(j));
        hash = zeros(1,K);
    for kk = 1:K
        chave = [chave num2str(kk)];
        hash(kk) = DJB31MA(chave,127);
    end
    MinHashValue(i,:) = min([MinHashValue(i,:); hash]);  % min value of the hash for a title
    end
end


shingle_size=3;
K = 150; % number of ;funções de dispersão’

MinHashSig = inf(length(dic),K);
for i = 1:length(dic)
    group = lower(dic{i,1});
    shingles = {};
    for j = 1 : length(group) - shingle_size+1  % shingles 
        shingle = group(j:j+shingle_size-1);
        shingles{j} = shingle;
end

for j = 1:length(shingles)
    chave = char(shingles(j));
    hash = zeros(1,K);
    for kk = 1:K
        chave = [chave num2str(kk)];
        hash(kk) = DJB31MA(chave,127);
    end
    MinHashSig(i,:) = min([MinHashSig(i,:);hash]);  % min hash Value min for this shingle
    end
end
%% save
save 'data' 'MinHashValue' 'MinHashSig' 'BF'


%% funtions Bloom Filter

function BF = init(n)
    BF = zeros(1,n);
end

function BF = insert(elemento, BF, k)
    n = length(BF);
    for i = 1:k
        elemento = [elemento num2str(i)];
        h = DJB31MA(elemento, 127);
        h = mod(h,n) + 1; %para dar valor entre 1 e n para por no BF
        BF(h) = BF(h) + 1;
    end
end

