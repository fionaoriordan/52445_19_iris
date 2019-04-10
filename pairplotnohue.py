# Fiona O'Riordan 09 Apr 2019
# Iris Data Project
# Script to show scatterplots for all of the variable combinations in the iris data set and histograms on the diagonal showing the distribution of each variable individually  WITHOUT the iris class 'species' represented by difference in color.
# Adapted from: 
# https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#title
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# https://stackoverflow.com/questions/29813694/how-to-add-a-title-to-seaborn-facet-plot
# https://stackoverflow.com/questions/47542104/how-to-control-the-legend-in-seaborn-python
# import the seaborn library so that we can use seaborn functions and rename as sns 
import seaborn as sns
# import the matplotlib library functions below  and rename as plt
import matplotlib.pyplot as plt

# load the iris data set from seaborn
iris = sns.load_dataset("iris")
# create a pairplot for the iris dataset with the iris data set class 'species' determing color and call it g
g = sns.pairplot(iris) 
# Seaborn calls the column 'Class' 'species'. Renaming on my output so there is no confusion
g._legend.set_title("Class")
# adjust the height of the title so it does not overlap the graph
plt.subplots_adjust(top=0.9)   
# create a chart subtitle.
g.fig.suptitle("Iris: Histogram & Scatterplot")
# output the figure created
plt.show()