import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_axes([0,0,1,1])

y = [20, 40, 10]
x = [10, 20, 30]
ax.plot(x, y, 'b-.', label='A-mavi')

y = [40, 10, 30]
x = [10, 20, 30]
ax.plot(x, y, 'r--', label='B-kırmızı')

ax.legend(loc=0)
ax.grid()
ax.set_title("İki farklı değer çizimi")