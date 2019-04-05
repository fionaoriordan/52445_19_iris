# Fiona O'Riordan 28 March 2019 
# Project Iris Data Set
# Show the Head and Tail rows of the  Iris Data Set
# Adapted from:
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
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

# See the first 25 rows of the data set, print to the screen
print(iris.head())

# Using to_csv to write the first 25 rows to an output file with  separator ',' to separate the data into columns
iris.head().to_csv("headirisoutput.csv", sep=',')




   






 


 