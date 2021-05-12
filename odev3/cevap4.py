import numpy as np
import matplotlib.pyplot as plt
numbers = np.arange(0, 4*np.pi, 0.01)

fig = plt.figure(figsize=(8,6))
ax = fig.add_axes([0,0,1,1])

#f(x)=3*sin(x)-cos(x)
new_numbers = [3*np.sin(n)-np.cos(n) for n in numbers]

ax.plot(new_numbers, label='f(x)=3*sin(x)-cos(x)')

# g(x)=2*cos(x)*sin(x)
new_numbers = [2*np.cos(n)*np.sin(n) for n in numbers]

ax.plot(new_numbers, 'r', label='g(x)=2*cos(x)*sin(x)')

ax.legend(loc=0)
ax.grid()