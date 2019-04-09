# **Fiona O'Riordan 28 March 2019
# **Module 52445 Programming and Scripting
# **Project Iris Data Set

![versicolor image](https://github.com/fionaoriordan/52445_19_iris/blob/master/220px-Iris_versicolor_3.jpg)[7]
![virginica image](https://github.com/fionaoriordan/52445_19_iris/blob/master/220px-Iris_virginica.jpg) [7]
![setosa image](https://github.com/fionaoriordan/52445_19_iris/blob/master/setosaimage.jpg)[6]

Due Date: 28th April 2019

## **Introduction**
This repository, 52445_proj_19 , is my submission for Project 2019, module 52445 Programming and Scripting.  The project is an exploration of Fisher’s Iris data set [1] including research on the data set, documentation and code in the Python programming language [2] based on that research.  

The project begins with background information on Fisher and the Iris Data Set.  Next, the prerequisites to using the python code within this project will be outlined. A list of contents of the repository will be provided including each of the python programs created for this project coupled with a brief overview of each of the scripts listed.  Instructions on how to execute the python code will also be detailed.  An exploratory data analysis summarizing the dataset will be included.  Lastly, appropriate references used throughout will be documented.


## **Background**

### **Fisher**
[1]
### **The Iris Data Set Creation**
 Botantist Dr. E. Anderson collected the Iris data which Fisher then used famously in his 1936 Analysis [2].  The data set contains 3 classes with each class representing a type of Iris flower specie[2]. The first two species Iris setosa and Iris versicolor were found growing together [2], while the third species, Iris Virginica separately was found separately [2]. For each class, 50 samples were collected.

 The data set is a multivariate data set and has four variables/features/attributes for each flower picked. The four variables measured for each sample collected were:
   1. sepal length in cm
   1. sepal width in cm
   1. petal length in cm
   1. petal width in cm
  This iris image shows the petal and sepal components of an Iris flower[5]![Iris image](https://github.com/fionaoriordan/52445_19_iris/blob/master/iris_with_labels.jpg) 
 
 

### **Fisher’s Analysis of the Iris Data Set**
 Fisher's analysis was published in The Use of Multiple Measurements in Taxonomic Problems, 1936 [2].  Fisher found that one class is linearly separable from the other two classes[3]. While the other two classes are not linearly separable from each other [3]. The dataset is infamous in the computer science field of pattern recognition [3]. 'Pattern recognition is one of the four cornerstones of Computer Science. It involves finding the similarities or patterns among small, decomposed problems that can help us solve more complex problems more efficiently' Verbatim(https://www.bbc.com/bitesize/guides/zxxbgk7/revision/1).


Class Setosa is linearly separable from classes Virginica and Vertosa. However, the classes Virginica and Vertosa are NOT linearly separable from each other [3] (https://archive.ics.uci.edu/ml/datasets/iris).  Define ‘Linear Separability’[4]
‘Linear separability refers to the fact that classes of patterns with -dimensional vector  can b e separated with a single decision surface. In the case above, the line  represents the decision surface.


## **To Download the Iris Data Set**
1. In your internet browser open [Kaggle.com Iris Data Set](https://www.kaggle.com/uciml/iris). 
1. Click on the link ![Download4KB](https://github.com/fionaoriordan/52445_19_iris/blob/master/kaggleirisdownload.png).
1. Register with site.
1. Open the now downloaded folder 'iris-species' in your Downloads folder on your computer.
1. You can now view the Iris Data set by clicking on the Iris.csv file.

## **Executing the python programs

1. In the [repository page 52445_19_iris](https://github.com/fionaoriordan/52445_19_iris/blob/master/iris_with_labels.jpg) click on Download Zip ![download Zip](image file required).
1. Once the repository has been saved to your downloads folder locally, then move to your desktop.
1. Launch your Command Line Interface (see above).
1. Open the Desktop directory with command: cd Desktop
1. Open the folder 52445_19_iris with command: cd 52445_19_iris
1. To run a script type python followed by the script name at the command line prompt e.g. python .py
1  script specific instructions…

## **Exploratory Data Analysis

This sections seeks to analyse the iris data set using python and produce a clear understanding of the data set.

* Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.
*  Write a summary of your investigations.
*  Include supporting tables and graphics as you deem necessary.
# **Overview 
1. shapeiris.py shows the iris data set/table has 150 rows and 5 columns:
![Shape](https://github.com/fionaoriordan/52445_19_iris/blob/master/shapeimage.png)


1. columnsiris.py shows the names of the 5 columns. The first four are attributes/variables collected by Anderson. The last column 'class' stores the iris flower class. Classes are  :

![Columns iris](https://github.com/fionaoriordan/52445_19_iris/blob/master/columnsimage.png)

1. classiris.py shows how many data points for each class are in the data set/table. The Iris data set is a balanced data set as each class is equally represented in the data set. There are 50 data points for each class.

1. ![Count by Class](https://github.com/fionaoriordan/52445_19_iris/blob/master/countclassimage.png)

1. headtailiris5.py shows the first and last 5 rows of the data set including the names assigned to each of the variables and the class.  ![Headtail image](https://github.com/fionaoriordan/52445_19_iris/blob/master/imgheadtail5.png)

Click here to view the [first 5 rows] in a searchable table(https://github.com/fionaoriordan/52445_19_iris/blob/master/head5irisout.csv)
Click here to view the [last 5 rows] in searchable table(https://github.com/fionaoriordan/52445_19_iris/blob/master/tail5irisout.csv)

1. desciris.py generates a statiscal summary of the dataset. For each of the four variables/columns the mean (average value), std (a value representing by how much the data of a variable differs from the mean value of that variable), min (the minimum value of the variable), max (the maximum value of the variable) and the percentiles 25%, 50% and 75% ( the nth percentile is the lowest value that is greater than n% of the values in a particular attribute)[8].  The output also shows that there are no missing values in any of the columns since all variables have a count = 150. 

![Desc Iris Screenshot](https://github.com/fionaoriordan/52445_19_iris/blob/master/descirisshot.png)

To view in a searchable table click on:

[Statisical Summary Table](https://github.com/fionaoriordan/52445_19_iris/blob/master/descirisoutput.csv)

 
1. Using python script irishist.py, we can see an approximate frequency distribution of each of the quantitative variables in the set i.e. how often each different value of the variables occurs (See Histogram1) [11, 12, 13]. Unlike variables sepal-width and sepal-length, we can see variables 'petal-width' and 'petal-length' could be interpreted as a bimodal distribution. A bimodal distribution is a distribution where there are two peaks [13]  This is interesting because it suggests there may be two distinct populations in the data set. 
![Histogram1](https://github.com/fionaoriordan/52445_19_iris/blob/master/Histogram1.png)

Similary, generating a scatter plot matrix 

However, we do know from classiris.py that we have 3 classes, namely Iris setosa, Iris versicolora and Iris virginica, in the data set. Therefore, the next step is to investigate the variables 'petal-width' and 'petal-length' more closely by including the classes in a histogram. 

Using histpetalclass.py [14](note: enter the py script name and the attribute name to run the report e.g. python histpetalclass.py 'petal-length'.), we can see that for variable petal-width class and petal-length the class/flowers Iris-setosa are clearly distinguished from Iris Versicolor and Iris Viginica. 
![Histogram petal-width by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_petal-width.png)
![Histogram petal-length by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_petal-length.png)

However, when we run classiris.py for sepal-width and again for sepal-length, we notice that no such distinction exists. The measurements for all three classes overlap and we cannot distinguish between the three classes.

![Histogram sepal-width by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_sepal-width.png)
![Histogram sepal-length by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_sepal-length.png)

![Pairplot of all variables with colour indicating class](https://github.com/fionaoriordan/52445_19_iris/blob/master/imgpairplot.png)


# **2-D scatter plot:


iris.plot(kind='scatter', x='sepal_length', y='sepal_width') ;
plt.show()

However, this is not helpful as we cannot decipher the class labels.
#What if we color the points by their class-label/flower-type??






##**References**
2. http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf
3. https://archive.ics.uci.edu/ml/datasets/iris
4. http://www.ece.utep.edu/research/webfuzzy/docs/kk-thesis/kk-thesis-html/node19.html
5. https://www.math.umd.edu/~petersd/666/html/iris_pca.html
6. http://www.twofrog.com/irissetosa.html
7. https://en.wikipedia.org/wiki/Iris_flower_data_set
8. https://www.statisticshowto.datasciencecentral.com/9. probability-and-statistics/percentiles-rank-range/
9. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
10. https://asq.org/quality-resources/histogram#types
11. https://www.youtube.com/watch?v=r75BPh1uk38
12. https://www.youtube.com/watch?v=J_k8_hA-KUE
13. https://en.wikipedia.org/wiki/Multimodal_distribution
14. https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples/
