# Fiona O'Riordan 28 March 2019 
# Project Iris Data Set
# Create histograms for the Iris Data Set
# Adapted from:
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://www.youtube.com/watch?v=r75BPh1uk38
# https://stackoverflow.com/a/19603918/11250489
# https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/37970713
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
plt.hist(bins=20)
# generate a file to output the graph
plt.show()

