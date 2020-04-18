clear;clc;close all;

load("ex4data1.mat");
load("ex4weights.mat");
[m,n] = size(X);        

sel = randperm(m);      %????trainingdata
sel = sel(1:100);
displayData(X(sel,:));

