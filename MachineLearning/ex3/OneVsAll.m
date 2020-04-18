function theta_back = OneVsAll(x,y,theta)
%ONEVSALL Summary of this function goes here
%   Detailed explanation goes here
    options = optimset('GradObj','on','MaxIter',500);
    n = size(theta);
    lambda = 3;
    theta_back = theta;
    for i = 1:10
        pos = find(y == i);
        neg = find(y ~= i);
        y_n = y;
        y_n(pos,:) = 1;
        y_n(neg,:) = 0;
        [thetaf,J,exitflag] = fminunc(@(t)(lrCostFunction(t,x,y_n,lambda)),theta,options);
        theta_back = [theta_back thetaf];
    end
    theta_back = theta_back(:,2:end);
        
end

