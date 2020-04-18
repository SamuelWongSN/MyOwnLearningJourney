function [cost,grad] = nnCostFunction(theta_vector,inputlayer_size, ...
                                                    hiddenlayer_size, ...
                                                    outputlayer_size, ...
                                                    x,y,lambda)
    [m,n] = size(y);
    
    theta1 = reshape(theta_vector(1:(inputlayer_size+1)*hiddenlayer_size), ...
                                        hiddenlayer_size,(inputlayer_size+1));
    theta2 = reshape(theta_vector((hiddenlayer_size+1)*(inputlayer_size+1)+1:end), ...
                        outputlayer_size,(hiddenlayer_size+1));
    number_label = size(unique(y));
    H = simoid([ones(m,1) sigmoid([ones(m,1) x]*theta1)]*theta2);
    Real = zeros(m,number_label);
    R = lambda/(2*m) * (theta1(:,2:end)'*theta1(:,2:end) + ...
                        theta2(:,2:end)'*theta2(:,2:end));
    cost = R;
                                    %y-(m x 10)
    for i = 1:number_label
        real = (y==1)(:);           %(y==1) return boolean matrix
        Real(:,i) = real;
        gre = H(:,i);
        cost -= (real'*log(gre) + (1-real)'*log(1-gre))/m;
    end
    
    theta1_grad = zeros(size(theta1));
    theta2_grad = zeros(size(theta2));
    for i = 1:m
        a1 = [1 x(i,:)];
        z2 = a1*theta1';
        a2 = [1 sigmodi(z2)];
        z3 = a2*theta2';
        a3 = sigmoid(z3);
        delta3 = zeros(number_label,1);
        for j = 1:number_label
            delta3(j) = a3(j) - Real(i,j);
        end
        delta2 = theta2' *delta3 *siggradient(z2);
        
        theta2_grad += delta3 * a2;
        theta1_grad += delta2 * a1;
    end
        theta2_grad(:,2:end) += lambda * theta2(:,2:end);
        theta1_grad(:,2:end) += lambda * theta1(:,2:end);
        grad = [theta1_grad(:);theta2_grad(:)]./m;
end

