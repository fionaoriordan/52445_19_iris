# Fiona O'Riordan 01 April 2019 
# Project Iris Data Set
# This script lists the names of five columns of the Iris data set.
# Adapted from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html?highlight=columns#pandas.DataFrame.columns [29]
import pandas as pd
# import sys library so that we can use function sys.argv 
import sys

# load the iris dataset. 
# In order to be able to work offline I have downloaded the set and added to the 52445_19_IRIS folder instead.
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'] 

# read in the iris.csv now saved locally, assign the names created above to the data as the attribute names/column headings.
iris = pd.read_csv("iris.csv",names=names)

print(iris.columns)
