function [J_val,theta] = GradDesL(x,y,theta,iter)
%GRADDESL Summary of this function goes here
%   Detailed explanation goes here
    m = length(y);
    J_val = zeros(iter,1);
    alpha = 0.001;
    for i = 1:iter
        grad  = x' * (x * theta - y) ./ m;
        theta = theta - alpha .* grad;
        J_val(i,:) = LRCFnonR(x,y,theta);
    end

end
