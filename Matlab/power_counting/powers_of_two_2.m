itterations=99
zeros=[0]
ones=[0]
twos=[0]
threes=[0]
fours=[0]
fives=[0]
sixs=[0]
sevens=[0]
eights=[0]
nines=[0]
for i = 0:itterations
    2^i
    [a0,b1,c2,d3,e4,f5,g6,h7,j8,k9] = f(int2str(2^i))
    zeros(length(zeros)+1)=a0+zeros(length(zeros))
    ones(length(ones)+1)=b1+ones(length(ones))
    twos(length(twos)+1)=c2+twos(length(twos))
    threes(length(threes)+1)=d3+threes(length(threes))
    fours(length(fours)+1)=e4+fours(length(fours))
    fives(length(fives)+1)=f5+fives(length(fives))
    sixs(length(sixs)+1)=g6+sixs(length(sixs))
    sevens(length(sevens)+1)=h7+sevens(length(sevens))
    eights(length(eights)+1)=j8+eights(length(eights))
    nines(length(nines)+1)=k9+nines(length(nines))
end
hold on
plot([0:itterations],zeros(2:itterations+2))
plot([0:itterations],ones(2:itterations+2))
plot([0:itterations],twos(2:itterations+2))
plot([0:itterations],threes(2:itterations+2))
plot([0:itterations],fours(2:itterations+2))
plot([0:itterations],fives(2:itterations+2))
plot([0:itterations],sixs(2:itterations+2))
plot([0:itterations],sevens(2:itterations+2))
plot([0:itterations],eights(2:itterations+2))
plot([0:itterations],nines(2:itterations+2))
xlim([0 10])
ylim([0 10])
hold off

function [a,b,c,d,e,f,g,h,j,k] = f(string)
    a=0;
    b=0;
    c=0;
    d=0;
    e=0;
    f=0;
    g=0;
    h=0;
    k=0;
    j=0;
    for i = 1:length(string)
        if(string(i)=='0')
            a=a+1;
        end
        if(string(i)=='1')
            b=b+1;
        end
        if(string(i)=='2')
            c=c+1;
        end
        if(string(i)=='3')
            d=d+1;
        end
        if(string(i)=='4')
            e=e+1;
        end
        if(string(i)=='5')
            f=f+1;
        end
        if(string(i)=='6')
            g=g+1;
        end
        if(string(i)=='7')
            h=h+1;
        end
        if(string(i)=='8')
            j=j+1;
        end
        if(string(i)=='9')
            k=k+1;
        end
    end
end
