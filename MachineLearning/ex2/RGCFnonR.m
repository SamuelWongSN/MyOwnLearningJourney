function [J_val,grad] = RGCFnonR(theta,x,y)
%RGCFNONR Summary of this function goes here
%   Detailed explanation goes here
    m = length(y);
    hx = Sigmoid(x * theta);
    J_val = -(y' * log(hx) + (1 - y)' * log(1-hx)) / m;
    grad = (hx-y)'*x ./ m;
end

