import matplotlib.pyplot as plt
import numpy as np

def f(x, m):
    return m*np.sin(x*(1/m))

x = np.linspace(0,10,100)

m_values = np.linspace(0,1,100)


y = f(x, m_values[-1])
lines = plt.plot(x,y)
max_f = f(x[-1], m_values[-1])
plt.axis([x[0], x[-1], -0.1, max_f])


for m in m_values:
    y = f(x,m)
    lines[0].set_ydata(y)
    plt.draw()
    plt.pause(0.01)
