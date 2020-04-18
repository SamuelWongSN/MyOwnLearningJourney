function W = randinitw(L_in, L_out)

espilon = 0.12;
W = rand(L_out, 1 + L_in)*espilon*2 - espilon;
end

