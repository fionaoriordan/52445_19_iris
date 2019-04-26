# Fiona O'Riordan 28 March 2019 
# Project Iris Data Set
# This script describes the Iris Data Set by showing the count, mean, standard deviation, minimum, maximum and percentile values for each of the four attributes in the set.
# Adapted from:
# https://www.statisticshowto.datasciencecentral.com/9. probability-and-statistics/percentiles-rank-range/ [15]
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html [16]
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ [18]
# import the pandas library and rename as pd 
import pandas as pd
# import sys library so that we can use function sys.argv 
import sys

# load the iris dataset. 
# In order to be able to work offline I have downloaded the set and added to the 52445_19_IRIS folder instead.
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# assign names to the attributes and assign class the name 'class'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'] 

# read in the iris.csv now saved locally, assign the names created above to the data as the attribute names/column headings.
iris = pd.read_csv("iris.csv",names=names)

# Create a statistical summary and print to the screen
print(iris.describe())

# Using to_csv to write the iris description to an output file with  separator ',' to separate the data into columns
iris.describe().to_csv("descirisoutput.csv", sep=',')





   






 


 