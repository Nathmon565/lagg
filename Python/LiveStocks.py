matplotlibImported = False
try:
	import matplotlib
	import matplotlib.pyplot as plt
	import matplotlib.animation as animation
	matplotlibImported = True
except ImportError:
	print("ERROR: Can't import matplotlib!")

import math
import time

#matplotlib.interactive(True)

updateInterval = 1000
seed = 1

def stockVal(time, seed, quality):
  x = time
  h_1 = seed
  h_2 = seed * seed
  k = quality
  
  sum = 0
  j = 0
  for j in range(0, k):
    sum +=((((x*math.pow(2,j))-math.floor(x*math.pow(2,j)))*((x*math.pow(2,j))-math.floor(x*math.pow(2,j)))*(3-2*((x*math.pow(2,j))-math.floor(x*math.pow(2,j)))))*((math.sin(math.floor((x*math.pow(2,j))+1)*h_1)*h_2)-math.floor((math.sin(math.floor((x*math.pow(2,j))+1)*h_1)*h_2)))+(1-(((x*math.pow(2,j))-math.floor(x*math.pow(2,j)))*((x*math.pow(2,j))-math.floor(x*math.pow(2,j)))*(3-2*((x*math.pow(2,j))-math.floor(x*math.pow(2,j))))))*((math.sin(math.floor(x*math.pow(2,j))*h_1)*h_2)-math.floor((math.sin(math.floor(x*math.pow(2,j))*h_1)*h_2))))/math.pow(2,j)
  
  return sum

import matplotlib.pyplot as plt
import matplotlib.animation as animation

#bounds of the graph
x_len = int(100)
y_range = [0, 2]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

# for i in range(x_len):
# 	ys[i] = stockVal((time.time()-i)/100, seed, 10)

#for i in range(ys.__len__()):
  #ys[i] = stockVal((time.time()-(60/(updateInterval/1000))*i), seed, 10)

line, = ax.plot(xs, ys)

plt.title('Stoque Marquet')
plt.xlabel('Samples')
plt.ylabel('Price')

def animate(i, ys):
    temp_c = stockVal(time.time()/100, seed, 10)

    ys.append(temp_c)
    ys = ys[-x_len:]
    line.set_ydata(ys)
    return line,

ani = animation.FuncAnimation(fig,animate,fargs=(ys,),interval=updateInterval,blit=True)

plt.show()
#plt.show(block=False)