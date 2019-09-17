import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15,30,45,10]
explode = (0,0.1,0,0)

fig, ax = plt.subplots()
ax.pie(sizes, explode = explode, labels=labels, autopct = '%1.1f%%', shadow = True, startangle = 90)

plt.show()