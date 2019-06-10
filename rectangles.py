import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation


fig=plt.figure()
titles = ["Abbas", "Rishi", "Sajan", "Shubham"]


y_pos = [2, 4, 6, 8]
scores = [0, 0, 0, 0]
end_scores = [100, 95, 10, 50]

plt.yticks(y_pos, titles)

plt.axis('equal')
ax = fig.add_subplot(111)
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)

patch = patches.Rectangle((0, 1.5), 1, 1)
patch2 = patches.Rectangle((0, 3.5), 1, 1)
patch3 = patches.Rectangle((0, 5.5), 1, 1)
patch4 = patches.Rectangle((0, 7.5), 1, 1)




def init():
    ax.add_patch(patch)
    ax.add_patch(patch2)
    ax.add_patch(patch3)
    ax.add_patch(patch4)    
    return []

def animate(i):
    patch.set_width(1+(i*0.25))
    patch2.set_width(1+(i*0.15))
    patch3.set_width(1+(i*0.2))
    patch4.set_width(1+(i*0.18))
    return []

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=100,
                               interval=50,
                               blit=True)
anim.save('rectangles.mp4', writer="ffmpeg")

plt.show()