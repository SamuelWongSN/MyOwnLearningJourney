function g = siggradient(f)
%SIGGRADIENT Summary of this function goes here
%   Detailed explanation goes here
    f = sigmoid(f);
    g = f.*(1-f);
end

