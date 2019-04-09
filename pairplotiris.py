# Fiona O'Riordan 09 Apr 2019
# Iris Data Project
# Script to show scatterplots for all of the variable combinations in the iris data set and histograms on the diagonal showing the distribution of each variable individually  with the iris class 'species' represented by difference in color.
# Adapted from: 
# https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset
# import the seaborn library so that we can use seaborn functions and rename as sns 
import seaborn as sns
# import the matplotlib library functions below  and rename as plt
import matplotlib.pyplot as plt

# load the iris data set from seaborn
iris = sns.load_dataset("iris")
# create a pairplot for the iris dataset with the iris data set class 'species' determing color.
sns.pairplot(iris, hue='species')
# output the figure created
plt.show()