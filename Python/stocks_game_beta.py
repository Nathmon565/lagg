import math

global market
market=[1000,500,250]
global phase
phase=1

def f(x,a):
    return sin(x^((a+10)/10))*(x)

def compute_stocks(phase):
    for i in range(len(market)):
        if(f(phase,i)>0):
            market(i)=market(i)+1
        if(f(phase,i)<0):
            market(i)=market(i)-1
