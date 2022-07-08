
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import pillow
r = 1
theta = np.arange(0,6.4,0.1)
xCircle0 = np.cos(theta)
yCircle0 = 1+np.sin(theta)
fig = plt.figure(figsize=(15,4))
ax = fig.add_subplot(autoscale_on=False,
    xlim=(1,10),ylim=(0,2))
ax.grid()
circle, = ax.plot(xCircle0,yCircle0,'-',lw=1)
point, = ax.plot([1],[1],'o')
trace, = ax.plot([],[],'-', lw=1)
theta_text = ax.text(0.02,0.85,'',transform=ax.transAxes)

textTemplate = '''x = %.1f°\n'''
xs,ys = [], []
def animate(x):

    if(x==0):
        xs.clear()
        ys.clear()
    xCycloid = x + r*np.cos(-x)
    #由于是向右顺时针滚，所以角度为负
    yCycloid = 1 + r*np.sin(-x)

    xCircle = xCircle0+x
    xs.append(xCycloid)
    ys.append(yCycloid)
    circle.set_data(xCircle,yCircle0)
    point.set_data([xCycloid],[yCycloid])
    trace.set_data(xs,ys)
    theta_text.set_text(textTemplate % x)
    return circle, point, trace, theta_text

frames = np.arange(0,10,0.02)
ani = animation.FuncAnimation(fig, animate, frames,
    interval=5, blit=True)
ani.save("Cycloid.gif")
plt.show()