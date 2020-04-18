clear;close all;clc;

 load("ex3data1.mat");
% %displayData(X,20);
[m,n] = size(X);
X = [ones(m,1) X];
% theta_init = zeros(n+1,1);
% 
% theta = OneVsAll(X,y,theta_init);
% r = predictOneVsAll(X(1,:),theta)

load("ex3weights.mat");