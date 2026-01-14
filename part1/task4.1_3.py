import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off') 

leg1 = patches.Rectangle((4.2, 3), 0.3, 1.2, facecolor='gray', edgecolor='black')
leg2 = patches.Rectangle((5.2, 3), 0.3, 1.2, facecolor='gray', edgecolor='black')
ax.add_patch(leg1)
ax.add_patch(leg2)

body = patches.Ellipse((5, 5), 3, 2, facecolor='lightblue', edgecolor='black')
ax.add_patch(body)

head = patches.Circle((3, 6), 1.2, facecolor='lightblue', edgecolor='black')
ax.add_patch(head)

eye = patches.Circle((2.7, 6.3), 0.3, facecolor='white', edgecolor='black')
pupil = patches.Circle((2.7, 6.3), 0.15, facecolor='black')
ax.add_patch(eye)
ax.add_patch(pupil)

beak = patches.Polygon([[2, 5.8], [1.5, 6], [2, 6.2]], facecolor='lightyellow', edgecolor='black')
ax.add_patch(beak)

wing = patches.Ellipse((5.5, 5), 1.5, 1, facecolor='blue', edgecolor='black', angle=30)
ax.add_patch(wing)

tail = patches.Polygon([[6.5, 5], [8, 4.5], [8, 5.5]], facecolor='blue', edgecolor='black')
ax.add_patch(tail)


plt.tight_layout()
plt.show()