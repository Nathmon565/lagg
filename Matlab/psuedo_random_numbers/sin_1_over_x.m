above=1;
below=1;
difference=[];
itterations=10000;
x_max=.000000021;
k=x_max/itterations;
outputs=[];
for i=1:itterations
    outputs(i)=sin(1/(k*i));
    if(sin(1/(k*i))>0)
        above=above+1;
    elseif(sin(1/(k*i))<0)
        below=below+1;
    end
    difference(i)=above-below;
end
scatter(1:itterations,difference,1,'black','filled');