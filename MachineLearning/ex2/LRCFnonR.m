function [J_val] = LRCFnonR(x,y,theta)
%LRCFNONR Summary of this function goes here
%   Detailed explanation goes here
    m = length(y);
    J_val = (x * theta - y)' * (x * theta - y);

end

