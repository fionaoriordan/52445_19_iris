# Fiona O'Riordan 09 Apr 2019
# Iris Data Project
# Script to show scatterplots for all of the variable combinations in the iris data set and histograms on the diagonal showing the distribution of each variable individually  WITHOUT the iris class 'species' represented by difference in color.
# Adapted from: 
# https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset [23]
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#title [24]
# https://seaborn.pydata.org/generated/seaborn.pairplot.html [25]
# https://stackoverflow.com/questions/29813694/how-to-add-a-title-to-seaborn-facet-plot [26]
# https://stackoverflow.com/questions/47542104/how-to-control-the-legend-in-seaborn-python [27]
# import the seaborn library so that we can use seaborn functions and rename as sns 
import seaborn as sns
# import the matplotlib library functions below  and rename as plt
import matplotlib.pyplot as plt

# load the iris data set from seaborn
iris = sns.load_dataset("iris")
# create a pairplot for the iris dataset with the iris data set class 'species' determing color and call it g
g = sns.pairplot(iris) 
# adjust the height of the title so it does not overlap the graph
plt.subplots_adjust(top=0.9)   
# create a chart subtitle.
g.fig.suptitle("Iris: Histogram & Scatterplot")
# output the figure created
plt.show()