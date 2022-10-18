% Ex4 
% nº n de pessoas

N = 1e5;
p = 0.5;

clear res
for people = 2: 366
    f = randi(365, people, N);
    for i = 1: N
        res(i) = length(unique(f(:, i))) < people;
    end
    prob = sum(res)/N;
    if (prob > p)
        people
        break
    end
end

