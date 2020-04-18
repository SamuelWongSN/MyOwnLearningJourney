function [cost,grad] = cFwithR(x,y,theta,lambda)
%CFWITHR Summary of this function goes here
%   Detailed explanation goes here
    m = length(y);
    n = size(theta);
    theta_t = theta(2:n);
    x1 = x(:,1);
    x_t = x(:,2:n);
    H = Sigmoid(x * theta);
    cost = -(y' * log(H) + (1-y)' * log(1-H)) /m + lambda* theta' *theta /2/m;
    grad_0 = x1' * (H-y)/m;
    grad_t = x_t' * (H-y)/m + lambda / m * theta_t;
    grad = [grad_0;grad_t];
end

