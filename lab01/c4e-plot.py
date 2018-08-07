import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1 Prepare data
labels = ["Web", "Androi", "iOS", "React Native"]
values = [400, 200, 250, 150]
colors = ["orange", "blue", "red", "pink"]
explode = [0,0,0,0.2]
# 2 Plot
pyplot.pie(
    values, 
    labels=labels, 
    colors=colors, 
    explode=explode
)
pyplot.axis('equal')

# 3 Show
pyplot.show()