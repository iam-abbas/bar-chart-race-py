import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random

fig=plt.figure()
titles = ["Abbas", "Rishi", "Sajan", "Shubham"]


y_pos = np.arange(len(titles))
scores = [0, 0, 0, 0]
end_scores = [100, 95, 10, 50]
rects = plt.barh(y_pos, scores)
ax = plt.subplot()
plt.xlim(0, 100)
plt.yticks(y_pos, titles)
def animate(i):
    if i == 99:
        titles = ["Abbas", "Rishi", "Sajan", "Shubham"]
        random.shuffle(titles)
        print(titles)
        ax.set_yticklabels(titles)
    for j, rect in enumerate(rects):
        if(i < end_scores[j]):
            rect.set_width(i)        
    return rects

anim = animation.FuncAnimation(fig, animate, blit=True, frames=100, interval=30)
anim.save('barh.mp4', writer="ffmpeg")


plt.show()