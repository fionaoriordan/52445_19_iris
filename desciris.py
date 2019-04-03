# Fiona O'Riordan 28 March 2019 
# Project Iris Data Set
# Describe the Iris Data Set
# Adapted from:
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# import the pandas library and rename as pd 
import pandas as pd
# import sys library so that we can use function sys.argv 
import sys

# load the iris dataset. 
# In order to be able to work offline I have downloaded the set and added to the 52445_19_IRIS folder instead.
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'] 

# read in the iris.csv now saved locally, assign the names created above to the data as the attribute names/column headings.
iris = pd.read_csv("iris.csv",names=names)

# Create a statistical summary 
irisdesc = iris.describe()

# create a txt file called "descirisoutput.txt" and write the iris description to the file overwriting any existing output.
# with open("descirisoutput.csv","w") as f:
#     f.write(str(irisdesc)
# Commented out the above and used to_csv instead as then I could use sep=',' and then the output data can be separated into columns.
irisdesc.to_csv("descirisoutput.csv", sep=',')
   






 


 