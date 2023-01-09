%%load
clc;
clear all;

load users.mat;
load movies.mat;
load noUsers.mat;
load eval.mat;
load BF.mat;
load data;

%% ask users id and validate it
id = 0;
fprintf(2,"Message: User's ID must be an integer!\n\n")
while id < 1 || id > 943 
    id = input('Insert User ID (1 to 943): ');
    if id < 1 || id > 943 
        fprintf("\nUser ID must be between 1 and 943!\n");
    end
end


%% Menu
menu = '\n1 - Your Movies\n2 - Suggestions of movies based on other users\n3 - Suggestion of movies based on already evaluated movies\n4 - Movies based on popularity\n5 - Exit\nChoice: ';
choice = input(menu);


% while choice is different from 5
while choice ~= 5
    if (choice < 1 || choice > 5)
           fprintf("\n%d is not a posible choice, try again:\n", choice)
           choice = input(menu);
    end
    switch choice
        case 1
            % ID's user movies
            fprintf("\nUser %d watched the following movies:\n\n",id);
            for i = 1:length(Set{id})
                fprintf('%d - %s\n', i, dic{Set{id}(i)});
            end
            fprintf(2, 'Press any key to continue.');
            pause; clc;  
            choice = input(menu);% present menu
        case 2
            getUserSuggestions(No, MinHashValue, id, Set, dic);
            pause; clc; 
            choice = input(menu);% present menu
        case 3
            getSuggestionEvMov(No, MinHashValue, id, Set, dic);
            pause; clc;    
            choice = input(menu);% present menu
        case 4
            popularMovies(id, dic, MinHashSig, eval, Set, BF)
            pause; clc;    
            choice = input(menu);% present menu
    end
end

%% GetUserSuggestions
function getUserSuggestions(No, MinHashValue, id, Set, dic)
    fprintf('\nPosible genres of Movies:\n  - Adventure\n  - Action\n  - Thriller\n  - Animation\n');
    fprintf('Calculating...\n')
    
    K = 100;  % mesmo número de funcoes de dispersão usados para a MinHash na database
    J = ones(1, No); 
    h = waitbar(0, 'Calculating...');
    for n = 1:No
        waitbar(n/No, h);
        if n ~= id
            J(n) = sum(MinHashValue(n,:) ~= MinHashValue(id,:))/K;  % dist de Jaccard 
        end
    end
    delete(h);

    [val1, SimilarUserId] = min(J);
    J(SimilarUserId) = inf;
    [val2, SimilarUserId2] = min(J);

    fprintf('\nMost similar user ID 1: %d\n', SimilarUserId);
    fprintf('\nMost similar user ID 2: %d\n', SimilarUserId2);
   
    sug = []; % suggestion
    for n = 1:length(Set{SimilarUserId})
        % if the similar user has a movie seen that current user hasn't
        if (~ismember(Set{SimilarUserId}(n), Set{id}))
            sug = [sug string(dic{Set{SimilarUserId}(n), 1})];
        end
    end

    for n = 1:length(Set{SimilarUserId2})
        % if the similar user has a movie seen that current user hasn't
        if (~ismember(Set{SimilarUserId2}(n), Set{id}))
            sug = [sug string(dic{Set{SimilarUserId2}(n), 1})];
        end
    end

    if isempty(sug)  
        fprintf('\nNo movies that werent evaluated!\n');
    else
       fprintf('\nNot evaluated movie titles: \n');
       for i = 1:length(sug)  % print suggested movies
           fprintf(sug(i) + '\n');
       end

    end
    fprintf(2, 'Press any key to continue. ');
    pause;
    clc;
end
%% GetSuggestionEvMovies
function getSuggestionEvMov(No, MinHashValue, id, Set, dic);
    K = 100;
    count = 0;

    for n1=1: length(Set{id})
        count = count + 1;
        aux = [];
        n1 = Set{id}(n1,1);
        J{count, 1} = n1;
        for n2= 1:No
            if(n2 ~= n1 && ~ismember(n2,Set{id}(:,1)))
                if n1 <= size(MinHashValue, 1)
                    jaccard = sum(MinHashValue(n1,:)~=MinHashValue(n2,:))/K;
                    if(jaccard <= 0.8)
                        aux = [aux n2];
                    end
                end
            end
        end
        J{count, 2} = aux;
    end

    counter = zeros(1,No);
    for h = 1: No
        for j=1:length(J)
            if(ismember(h, J{j, 2}))
                counter(:,h) = counter(:,h) + 1;
            end
        end
    end

    [~, sortedJ] = sort(counter);
    % pick 2 more similar 
    fprintf(dic{sortedJ(end)} + "\n");
    fprintf(dic{sortedJ(end-1)} + "\n");
    pause;
end

%% GetPopularMovies
function popularMovies(id, dic, MinHashSig, grades, Set, BF)
    str = lower(input('\nMovie: ', 's'));
    shingle_size = 3;  % Use the same number of shingles as in the database
    K = size(MinHashSig, 2);  % Use the same K as in the database for the movie title shingles
    threshold = 3;  


    % Cell array with shingles of the input string
    shinglesAns = {};
    for i = 1:length(str) - shingle_size+1
        shingle = str(i:i+shingle_size-1);
        shinglesAns{i} = shingle;
    end

    % Calculate MinHash signature for the input string
    MinHashString = inf(1,K);
    for j = 1:length(shinglesAns)
        chave = char(shinglesAns{j});
        hash = zeros(1,K);
        for kk = 1:K
            chave = [chave num2str(kk)];
            hash(kk) = DJB31MA(chave, 127);
        end
        MinHashString(1,:) = min([MinHashString(1,:); hash]);
    end

     % Distancia de Jaccard 
    distJ = ones(1, size(dic,1));
    h = waitbar(0,'Calculating');
    for i=1:size(dic, 1)  
        waitbar(i/K, h);
        distJ(i) = sum(MinHashSig(i,:) ~= MinHashString)/K;
    end
    delete(h);

    % Find the movie titles with the most similar MinHash signatures
    found = false;
    for i = 1:5
        [val, pos] = min(distJ);  % calculate min valor (+similar)
        if (val <= threshold)  %
            found = true;
            fprintf('%s   (%.2f) number of evaluations: %d\n', dic{pos, 1}, dic{Set{id}(i)}, insert(Set{id}(i), BF, threshold ) );
        end
        distJ(pos) = 3;  %  remove movie
    end
        % Find the MinHash signature with the smallest difference from the input string's signature
        %diffs = sum(MinHashSig ~= MinHashString, 2);
        %[minDiff, minDiffPos] = min(diffs);
        
        % Calculate the number of times the movie was rated 3 or above
        %if minDiffPos > size(grades,2)
        %    return
        %end

       % numGrades3Plus = sum(grades(:,minDiffPos) >= 3);
    
    if (~found)
        fprintf('No movies found.\n');
    end
    %fprintf(2, 'Press any key to continue. ');
    pause;clc; 

    % bloom filter function
    function BF = insert(elemento, BF, k)
        n = length(BF);
        for i = 1:k
            elemento = [elemento num2str(i)];
            h = DJB31MA(elemento, 127);
            h = mod(h,n) + 1; % 1-n
            BF(h) = BF(h) + 1;
        end
    end
end
