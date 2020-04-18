function [x1] = NorFea(x)
%NORFEA Summary of this function goes here
%   Detailed explanation goes here
    [m,n] = size(x);
    x1 = ones(m,1);
    for i = 1:n
        avg = mean(x(:,i));
        s   = std(x(:,i));
        x1  = cat(2,x1,(x(:,i)-avg)/s);
    end
end

