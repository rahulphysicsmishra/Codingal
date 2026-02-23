import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,11,1)
y1=(2*x)+1
y2=(2*x**x)+2
plt.plot(x,y1,'g',linewidth=3,label='y=2x+1')
plt.plot(x,y2,'r',linewidth=3,label='y=2x^2+2')
plt.legend()
plt.show()