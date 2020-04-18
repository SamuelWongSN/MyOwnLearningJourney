function [J_val,theta] = GradDesR(x,y,theta,iter)
%GRADDESR Summary of this function goes here
%   Detailed explanation goes here
    m = length(y);
    J_val = zeros(iter,1);
    alpha = 0.01;
    for i = 1:iter
        grad  = x' * (Sigmoid(x * theta) - y) ./ m ;
        theta = theta - alpha * grad;
        J_val(i,:) = RGCFnonR(x,y,theta);
    end
end

