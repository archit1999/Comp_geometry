import matplotlib.pyplot as plt
import random
from ric_algo import ric

a = []
b = []
for i in range(100):
    a.append(random.randint(1, 500))
    b.append(random.randint(1, 500))

c1 = ric(a, b)
plt.xlim(-1000, 1000)
plt.ylim(-1000, 1000)

c = plt.Circle((c1.centre.x, c1.centre.y), radius=c1.rad, alpha=0.7)

ax = plt.gca()
ax.add_patch(c)
plt.axis('scaled')
plt.scatter(a, b, color='r', alpha=0.5)

plt.show()
