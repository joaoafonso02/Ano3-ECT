function[y1] = distancia(x1, x2)

    y1 = sqrt(sum((x1-x2).^2));
end