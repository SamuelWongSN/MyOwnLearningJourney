clear;close all;clc;
dataex11 = load(".\ex1\ex1data1.txt");
dataex12 = load(".\ex1\ex1data2.txt");
%---------Simple Linear Regression-------------------
    y1  = dataex11(:,2);
    x10 = ones(length(y1),1);
    x11 = dataex11(:,1);
    x1  = cat(2,x10,x11);

    theta_init = [0;0];
    iter = 500;

    [J_val,theta] = GradDesL(x1,y1,theta_init,iter);

   
    
    subplot(2,1,1),plot(x11,y1,'x');
           hold on;plot(x11,x1*theta,'-');hold off;
    subplot(2,1,2),plot(J_val);
    pause;

%----------------Multiple Linear Regression-------

    x2 = dataex12(:,1:2);
    y2 = dataex12(:,3);
    x2 = NorFea(x2);
    [m2,n2] = size(x2);
    theta_init2 = zeros(n2,1);
    iter2 = 2000;
    
    [J_val2,theta2] = GradDesL(x2,y2,theta_init2,iter2);
    
    plot(J_val2);
    
 %-----------Normal Equation-----------------------
    thetaNE = pinv(x2' * x2) * x2' * y;
    