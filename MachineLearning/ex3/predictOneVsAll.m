function result = predictOneVsAll(x,theta)
%PREDICTONEVSALL Summary of this function goes here
%   Detailed explanation goes here

    result = find(sigmoid(x * theta) >= 0.5) -1;
    
end

