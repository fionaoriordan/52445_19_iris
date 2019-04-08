# Fiona O'Riordan 07 April 2019
# # Adapted from https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples/

# import sys library so that we can use function sys.argv
import sys
# import pandas library so that we can use panda functions and rename as pd 
import pandas as pd
# import the matplotlib library class pyplot in order to use the show function below and rename as plt
import matplotlib.pyplot as plt 

# Assign names to the attributes/variables and changed class name to classes as otherwise iris.class became an issue
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'classes'] 
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"  not using url as I have to work offline sometimes
# load the data by reading in the iris csv
iris = pd.read_csv("iris.csv", names=names)


# if two arguments are entered by the user i.e. the program name and the attribute/variable name e.g. petal-width, petal-length
if len(sys.argv) == 2:
#     # then the irisattribute is set to be the value of the second argument entered and the script is run for that attribute
    irisattribute = sys.argv[1]
    # Otherwise the script is run using petal-width as the irisattribute 
else:
    irisattribute = 'petal-width'


x1 = iris.loc[iris.classes=='Iris-setosa', irisattribute]
x2 = iris.loc[iris.classes=='Iris-versicolor', irisattribute]
x3 = iris.loc[iris.classes=='Iris-virginica', irisattribute]
 
# kwargs allows us to set parameters that we will us for each class/plt.hist
# the dict function allows us to return the key and value e.g. bins and 20  
# # alpha=0.5 fades the bars in the histogram and thereby,allows us to view overlap in bars 
# the default number of bins =10 but set the number of bins = 20 so that we can see the data grouped into smaller ranges.
# plt.hist(bins=20)
kwargs = dict(bins=20, alpha=0.5)

# setting the graph name
plt.figure(f'Hist {irisattribute}')
# creating histogram bars for the irisattribute variable by class with distinct colors for each class and the kwargs arguments defined above
plt.hist(x1, **kwargs, color='r', label='Iris-setosa')
plt.hist(x2, **kwargs, color='g', label='Iris-versicolor')
plt.hist(x3, **kwargs, color='b', label='Iris-virginica')
# setting a global value for the graph's title and labels
plt.gca().set(title=f'Frequency Histogram by class for  {irisattribute}', ylabel='Frequency', xlabel='Number of irises /range')
# setting the legend on the graph ie. the labels entered.
plt.legend()
# generating a graph file to show
plt.show()