difference=[];
itterations=10000;
lines=10;
for r=1:lines
    above=1;
    below=1;
    for i=1:itterations
        if(sin(randi(itterations))>0)
            above=above+1;
        elseif(sin(randi(itterations))<0)
            below=below+1;
        end
        difference(r,i)=above-below;
    end
end
hold on
for r=1:lines
    scatter(1:itterations,difference(r,:),1,[abs(sin(r)),abs(sin(r+2*pi/3)),abs(sin(r+4*pi/3))],'filled');
end
hold off
