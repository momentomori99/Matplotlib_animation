import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(0, 10*np.pi, 0.01)
y = np.sin(x)

fig = plt.figure()
ax = plt.subplot(1,1,1)

data_skip = 2
print(float(np.linspace(0,3142,3142)))



#called at the beginning at the animation and every time it repeats
def init_func():
    ax.clear()
    plt.xlabel('pi')
    plt.ylabel('func')

def update_plot(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
#
#
# anim = FuncAnimation(fig, update_plot, frames=np.linspace(0,len(x), len(x)), init_func=init_func, interval=20)
#
# plt.show()
