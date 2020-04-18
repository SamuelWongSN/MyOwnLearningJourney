function [cost,grad] = lrCostFunction(theta,x,y,lambda)
    [m,n] = size(x);
    H = sigmoid(x * theta);
    theta_t = theta(2:end,:);
    cost = -1/m * (y' * log(H) + (1 - y)' * log(1 - H)) + lambda/(2*m) * theta_t' * theta_t;
    
    theta_t = theta(2:end,:);
    x_0 = x(:,1);
    x_t = x(:,2:end);
    
    grad_0 = 1/m * x_0' * (H - y);
    grad_t = 1/m * x_t' * (H - y) + lambda/m * theta_t;
    grad = [grad_0 ; grad_t];
end

% function [J, grad] = lrCostFunction(theta, X, y, lambda)
% %LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
% %regularization
% %   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
% %   theta as the parameter for regularized logistic regression and the
% %   gradient of the cost w.r.t. to the parameters. 
% 
% % Initialize some useful values
% % Initialize some useful values
% m = length(y); % number of training examples
% n = size(theta);
% % You need to return the following variables correctly 
% theta_t = theta(2:n);
% X1 = X(:, 1);
% X_t = X(:, 2:n);
% H = sigmoid(X*theta);
% J = -(y'*log(H) + (1-y)'*log(1-H)) / m + lambda * theta_t' * theta_t / (2*m);
% grad = (X_t'*(H-y) + lambda * theta_t) ./ m;
% grad1 = X1'*(H-y) / m;
% grad = [grad1; grad];
% 
% % ====================== YOUR CODE HERE ======================
% % Instructions: Compute the cost of a particular choice of theta.
% %               You should set J to the cost.
% %               Compute the partial derivatives and set grad to the partial
% %               derivatives of the cost w.r.t. each parameter in theta
% %
% % Hint: The computation of the cost function and gradients can be
% %       efficiently vectorized. For example, consider the computation
% %
% %           sigmoid(X * theta)
% %
% %       Each row of the resulting matrix will contain the value of the
% %       prediction for that example. You can make use of this to vectorize
% %       the cost function and gradient computations. 
% %
% % Hint: When computing the gradient of the regularized cost function, 
% %       there're many possible vectorized solutions, but one solution
% %       looks like:
% %           grad = (unregularized gradient for logistic regression)
% %           temp = theta; 
% %           temp(1) = 0;   % because we don't add anything for j = 0  
% %           grad = grad + YOUR_CODE_HERE (using the temp variable)
% %
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% % =============================================================
% 
% grad = grad(:);
% 
% end
