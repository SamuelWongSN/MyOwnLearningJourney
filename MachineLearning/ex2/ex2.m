clear;close all;clc;
dataex21 = load('.\ex2\ex2data1.txt');
dataex22 = load('.\ex2\ex2data2.txt');

[m1,n1] = size(dataex21);
x1 = [ones(m1,1) dataex21(:,1:2)];
y1 = dataex21(:,3);


theta_init = zeros(n1,1);
%RGCFnonR(x1,y1,theta_init)
iter = 2000;
%[J_val,theta] = GradDesR(x1,y1,theta_init,iter);

options = optimset('GradObj','on','MaxIter',400);%fun????gradient
[theta, cost] = ...
	fminunc(@(t)(RGCFnonR(t,x1,y1)), theta_init, options);
RGCFnonR(theta,x1,y1)
Sigmoid([1,45,85]*theta)
pos = find(y1 == 1);neg = find(y1 == 0);%return index

figure;
hold on;
plot(x1(pos,2),x1(pos,3),'k+');%use index ???
plot(x1(neg,2),x1(neg,3),'ko');
plotDB(x1,y1,theta);
hold off;

%----------Regularized logistic regression---------------

[m2,n2] = size(dataex22);
x2 = [ones(m2,1) dataex22(:,1:2)];
y2 = dataex22(:,3);
degree = 6;             %????6??

theta_init = zeros(28,1);
lambda = 1;

x2p = mapfeature(x2,degree);
cFwithR(x2p,y2,theta_init,lambda)

options = optimset('GradObj','on','MaxIter',400);
[theta2,grad] = fminunc(@(t)(cFwithR(x2p,y2,t,lambda)),theta_init,options)



pos2 = find(y2 == 1);neg2 = find(y2 == 0);
figure;hold on;
plot(x2(pos2,2),x2(pos2,3),'k+');
plot(x2(neg2,2),x2(neg2,3),'ko');
plotDB(x2p,y2,theta2);
hold off;

