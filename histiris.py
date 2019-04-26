# Fiona O'Riordan 28 March 2019 
# Project Iris Data Set
# Create histograms for all 4 variables in the data set distinctly showing an approximate frequency distribution of each of the quantitative variables in the set.
# Adapted from:
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ [18]
# https://www.youtube.com/watch?v=r75BPh1uk38 [19]
# https://stackoverflow.com/a/19603918/11250489 [20]
# https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/37970713 [21]
# import the pandas libary in order to use the read_csv function below and rename as pd 
import pandas as pd
# import the matplotlib library class pyplot in order to use the show function below and rename as plt
import matplotlib.pyplot as plt


# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" 
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'] 
# load the data by reading in the iris csv
iris = pd.read_csv("iris.csv", names=names)

# create a histogram for all the 4 variables 
# the default number of bins =10 but set the number of bins = 20 so that we can see the data grouped into smaller ranges.
# plt.hist(bins=20)

# creating the histograms for all 4 variables distinctly so that I can label 
# and color each chart distinctly

# name the output file 
plt.figure('Histogram1')
plt.subplot(2,2,1)
iris['petal-width'].hist(bins=20)
# x axis is from 0 to 5, y axis is from 0 to 18 with intervals of 1
# create an x axis label
plt.xlabel('range')
# create a y axis label
plt.ylabel('frequency')
plt.title('petal-width')


plt.subplot(2,2,2)
iris['petal-width'].hist(bins=20)
# x axis is from 0 to 5, y axis is from 0 to 18 with intervals of 1
# create an x axis label
plt.xlabel('range')
# create a y axis label
plt.title('petal-length')

plt.subplot(2,2,3)
iris['sepal-length'].hist(bins=20)
# create x axis label
plt.xlabel('range')
# create an y axis label
plt.ylabel('frequency')
plt.title('sepal-length')

plt.subplot(2,2,4)
iris['sepal-width'].hist(bins=20)
# create an x axis label
plt.xlabel('range')
# create an y axis label
plt.ylabel('frequency')
plt.title('sepal-width')


# generate a file to output the graph
plt.show()

