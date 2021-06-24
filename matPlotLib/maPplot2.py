import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4,4,.1)
y = x*x
y2 = x*x+2
plt.grid(True) # arkaplanda grid
plt.xlabel("X val") # x title
plt.ylabel("Y val") # y title
plt.title("Test title") # title

plt.plot(x,y,'b:', label="Grafik 1")
plt.plot(x,y2,'r*', label="Grafik 2")
plt.legend() # labelin konumu
#plt.plt(x,y,'-*')
# buarda * noktalı gösterim için 
# - aralara çizgi çekmek için 
# ya da renk yazılabilir.
plt.show()