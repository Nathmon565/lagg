sequence=[.00000000001,1];
above=1;
below=1;
difference=[];
itterations=1000;
for i=3:itterations
    sequence(i)=sequence(i-1)+sequence(i-2);
    if(sin(sequence(i))>0)
        above=above+1;
    elseif(sin(sequence(i))<0)
        below=below+1;
    end
    difference(i)=above-below;
end
scatter(1:itterations,difference,3,'black','filled');
