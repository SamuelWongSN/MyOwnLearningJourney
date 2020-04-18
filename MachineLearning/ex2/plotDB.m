function plotDB(x,y,theta)
%PLOTDB Summary of this function goes here
%   Detailed explanation goes here
    if size(x,2) <= 3
        plot_x = [min(x(:,2))-2 , max(x(:,2))+2];
        plot_y = (-1./theta(3)).*(theta(2).*plot_x+theta(1));
        plot(plot_x,plot_y);
    else
        u = linspace(-1,1.5,50);
        v = linspace(-1,1.5,50);
        z = zeros(length(u),length(v));
        
        for i = 1:length(u)
            for j = 1:length(v)
                z(i,j) = mapfeature([1,u(i),v(j)],6) * theta;
            end
        end
        
        z = z';
        contour(u,v,z,[0,0],'lineWidth',2);
end

