function [x] = mapfeature(x,degree)
%MAPFEATURE Summary of this function goes here
%   Detailed explanation goes here
    m = length(x);
    for i = 2:degree
        for j = 0:i
            x = [x x(:,2).^j .* x(:,3).^(i-j)];
        end
    end
end

