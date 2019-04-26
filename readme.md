# **Fiona O'Riordan 28 March 2019**
# **Module 52445 Programming and Scripting**
# **Project Iris Data Set**

![versicolor image](https://github.com/fionaoriordan/52445_19_iris/blob/master/220px-Iris_versicolor_3.jpg)[1]
![virginica image](https://github.com/fionaoriordan/52445_19_iris/blob/master/220px-Iris_virginica.jpg) [1]
![setosa image](https://github.com/fionaoriordan/52445_19_iris/blob/master/setosaimage.jpg)[2]

Due Date: 28th April 2019

## **Introduction**

This repository, 52445_proj_19 , is my submission for Project 2019, module 52445 Programming and Scripting.  The project is an exploration of Fisher’s Iris data set [1] including research on the data set, documentation and code in the Python programming language based on that research.  

The project begins with background information on Fisher, the Iris Data Set Creation and Fisher's Analysis of the Data. Instructions on how to download the Iris Data Set will then be detailed.  Next, a list of contents of the repository coupled with a brief overview of each of the scripts listed.  Steps to execute the python code within this project will also be detailed.   The Exploratory Data Analysis section will summarize the iris data and explore and document observable patterns within the data set using the repository scripts. Lastly, appropriate references used throughout will be documented.


## **Background**

### **Fisher**

Sir Ronald A. Fisher (1890 - 1962) was a British mathematician, statistician, evolutionary biologist and geneticist. 
>'R.A. Fisher's extraordinary contributions to statistical theory and methods, experimental design, scientific inference, evolutionary biology and genetics have had far-reaching consequences in many branches of human thought and endeavour'[4].

However, Fisher is also unfortunately famously known for his deeply held belief and role in the Eugenics movement (Pfeiffer,1994) [5]. The term eugenic was devised by Francis Galton (1883)[6] to denote “well born” (cited in Shakespeare, 2008: 22) [7].  

Proponents of eugenics believed that social advantage had a genetic hereditary basis. Society would benefit by ‘checking’ the reproduction of the ‘bad’, whilst promoting reproduction in the ‘good’ (Galton, 1869:41)[6].  Twentieth century actual implementations of eugenic thinking included forced sterilization in the US, UK and some Scandinavian countries (Kerr and Shakespeare, 2002, Barnes and Mercer, 2003)[8],[9].  The ultimate extreme of eugenic thinking was actualised in Nazi Germany when an estimated 250,000 disabled people and social undesirables were systematically murdered (Barnes and Mercer, 2003)[9].

So while we can acknowledge and benefit from Fisher's work as a statistician in this project, it is salient to remember science is neither created or used in a social or moral vacuum. 

### **The Iris Data Set Creation**

Botantist Dr. E. Anderson collected the Iris data which Fisher then used in his 1936 Analysis [3].  

The data set is a multivariate data set and has four variables/features/attributes for each flower picked. The four variables measured for each sample collected were:
   1. sepal length in cm
   1. sepal width in cm
   1. petal length in cm
   1. petal width in cm

This iris image shows the petal and sepal components of an Iris flower [14].

![Iris image](https://github.com/fionaoriordan/52445_19_iris/blob/master/iris_with_labels.jpg)

The data set contains three classes with each class representing a type of Iris flower specie[3]. The first two species Iris setosa and Iris versicolor were found growing together [3], while the third specie, Iris Virginica separately was found separately [3]. For each class, 50 samples were collected. Therefore 150 separate observations were recorded.

### **Fisher’s Analysis of the Iris Data Set**

Fisher's analysis was published in The Use of Multiple Measurements in Taxonomic Problems, 1936 [3].  Fisher found that class Iris Setosa is linearly separable from the other two classes Iris Virginica and Iris Vertosa [10]. While the later two classes are not linearly separable from each other [10]. 'Linear separability refers to the fact that classes of patterns with n-dimensional vector x = (x_1, x_2, ... , x_n) can be separated with a single decision surface'[11]. In other words, two classes are linearly separable when a line connecting a series of points can be draw between classes projected on to a surface[11],[12]. This chart shows how an example of gender classification (Female = Red, Male = Blue) is linearly separable based on height and weight:

![Example of Linear Separability](https://github.com/fionaoriordan/52445_19_iris/blob/master/linearlyseparable.png)[12]

The iris dataset is infamous in the computer science field of pattern recognition [10]. 'Pattern recognition is one of the four cornerstones of Computer Science. It involves finding the similarities or patterns among small, decomposed problems that can help us solve more complex problems more efficiently'[13]. Pattern recognition focuses on how a computer can be trained to read, interpret and distinguish between the differences of things and then categorize those things based on the patterns identified [31].

## **To Download the Iris Data Set**

1. In your internet browser open https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
1. Click on iris.data and the data set will be saved to your Downloads folder.
1. Save the file as iris.csv file.
1. Now open iris.csv in Excel (Windows) or Numbers(Mac)

## **Executing the python programs**
1. In the [repository page 52445_19_iris](https://github.com/fionaoriordan/52445_19_iris) click on Download Zip ![download Zip](https://github.com/fionaoriordan/52445_19_iris/blob/master/download_iris_repository.png).
1. Once the repository has been saved to your downloads folder locally, then move to your desktop.
1. Launch your Command Line Interface.
1. Open the Desktop directory with command: cd Desktop
1. Open the folder 52445_19_iris with command: cd 52445_19_iris
1. To run a script type python followed by the script name at the command line prompt e.g. python .py

## **Repository Contents (Scripts) & description

1. [shapeiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/shapeiris.py) shows the number of rows and columns in the Iris Data Set.
1. [columnsiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/columnsiris.py) lists the names of five columns of the Iris data set.
1. [classiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/classiris.py) lists the three classes in the dataset.
1. [headtailiris5.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/head5irisout.csv) shows the head and tail rows of the  Iris Data Set.
1. [desciris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/desciris.py) describes the Iris Data Set by showing the count, mean, standard deviation, minimum, maximum and percentile values for each of the four attributes in the set.
1. [histiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/histiris.py) Create histograms for all 4 variables in the data set to showing an approximate frequency distribution of each of the quantitative variables in the set.
1. [pairplotnohue.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/pairplotnohue.py) generates scatterplots for all of the variable combinations in the iris data set coupled with histograms on the diagonal showing the distribution but does not use any class information in its representation.
1. [histpetalclass.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/histpetalclass.py) creates histograms for the Iris Data Set with each of the 3 classes distinguished by colour.
1. [pairplot.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/pairplotiris.py) generates scatterplots for all of the variable combinations in the iris data set and histograms on the diagonal showing the distribution of each variable individually  with the iris class 'species' represented by difference in color.


## **Exploratory Data Analysis**

This sections seeks to analyse the iris data set using python and produce a clear understanding of the data set.

### **Data Summary** 

1. Iris data set/table has 150 rows and 5 columns as demonstrated by [shapeiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/shapeiris.py):![Shape](https://github.com/fionaoriordan/52445_19_iris/blob/master/shapeimage.png)
1. The names of five column of the Iris data set are shown by  [columnsiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/columnsiris.py). The first four are attributes/variables collected by Anderson and the last column 'class' stores the iris flower class: ![Columns iris](https://github.com/fionaoriordan/52445_19_iris/blob/master/columnsimage.png)
1. As [classiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/classiris.py) shows, the dataset has three iris classes: Iris Setosa, Iris-virginica and Iris-versicolor. The Iris data set is a balanced data set as each class is equally represented within the data set as there are 50 observations for each class recorded witin the class.
![Count by Class](https://github.com/fionaoriordan/52445_19_iris/blob/master/countclassimage.png)
1. Python scripts headtailiris5.py shows the first and last 5 rows of the data set including the names assigned to each of the variables and the class are shown by [headtailiris5.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/headtailiris5.py).  
![Headtail image](https://github.com/fionaoriordan/52445_19_iris/blob/master/imgheadtail5.png) 
Click here to view the [first 5 rows] in a searchable table:[head5irisout.csv](https://github.com/fionaoriordan/52445_19_iris/blob/master/head5irisout.csv) 
and click here to view the last 5 rows in searchable table[tail5irisout.csv](https://github.com/fionaoriordan/52445_19_iris/blob/master/tail5irisout.csv)
1. A statistical summary of the iris data set is generated by  [desciris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/desciris.py)[16]. For each of the four variables/attributes the mean (average value), std (a value representing by how much the data of a variable differs from the mean value of that variable), min (the minimum value of the variable), max (the maximum value of the variable) and the percentiles 25%, 50% and 75% ( the nth percentile is the lowest value that is greater than n% of the values in a particular attribute)[n].  The output also shows that there are no missing values in any of the columns since all variables have a count = 150.  ![Desc Iris Screenshot](https://github.com/fionaoriordan/52445_19_iris/blob/master/descirisshot.png). 
To view in a searchable table click on: [Statisical Summary Table](https://github.com/fionaoriordan/52445_19_iris/blob/master/descirisoutput.csv)

### **Observable Patterns within the Iris Data Set**

Now it is time to look for any interesting patterns or observations within the iris data set.

**A suggestion of distinct populations:**

1. An approximate frequency distribution of each of the quantitative variables in the set is generated by python script [histiris.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/histiris.py)[19] [20] [21].  How often each range of values occurs by variable is plotted.![Histogram1](https://github.com/fionaoriordan/52445_19_iris/blob/master/Histogram1.png).  
Unlike variables sepal-width and sepal-length, we can see variables 'petal-width' and 'petal-length' could be interpreted as a bimodal distribution. A bimodal distribution is a distribution where there are two peaks [22]. This distribution is interesting because it suggests there may be two distinct populations in the data set.
1. Similary, generating a scatter plot and histogram matrix, using [pairplotnohue.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/pairplotnohue.py), we can see when using variable petal_width and/or petal_length a similiar distinction within the data set is suggested by scatter plots as histograms. However, again, when the two dimensional variable combinations do NOT include petal_width and/or petal_length, we do not see a suggestion of a distinction within the data. Scatterplots for joint relationships and histograms for univariate distributions:![hist_scatter_nohue.png](https://github.com/fionaoriordan/52445_19_iris/blob/master/hist_scatter_nohue.png)

**Color provides an explanation**

However, we do know from [classiris.py]((https://github.com/fionaoriordan/52445_19_iris/blob/master/classiris.py)),as discussed earlier,that we have 3 classes, namely Iris-setosa, Iris-versicolora and Iris-virginica, in the data set. Therefore, the next step is to investigate the data more closely by including 'class' in our analysis. Color will used to denote iris class.

1. Using [histpetalclass.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/histpetalclass.py)[17],(note: enter the py script name followed by the variable name to run the report e.g. python histpetalclass.py 'petal-length'.), we can see that for variable petal-width class and petal-length the class/flowers Iris-setosa are clearly distinguished from Iris Versicolor and Iris Viginica.
![Histogram petal-width by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_petal-width.png)![Histogram petal-length by class](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_petal-length.png)
1. However, when we run histpetalclass.py for sepal-width and again for sepal-length, we notice that no such distinction exists in measurement. The measurements for all three classes overlap. ![Hist_sepal-width.png](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_sepal-width.png)
![Hist_sepal-length.png](https://github.com/fionaoriordan/52445_19_iris/blob/master/Hist_sepal-length.png)
1. As the python script [pairplot.py](https://github.com/fionaoriordan/52445_19_iris/blob/master/pairplotiris.py), shows class Iris Setosa can be clearly separated from classes Iris Virginica and Iris Vertosa when at least one of the two variables in a two dimensional variable combination is a petal measurement.![imgpairplot.png](https://github.com/fionaoriordan/52445_19_iris/blob/master/imgpairplot.png). This separation does not exist when 
 **both** variables are sepal measurements and classes Iris Virginica and Iris Vertosa are not linearly separable regardless of variables projected.

## **References**

1. Wikipedia, Iris flower data set.
https://en.wikipedia.org/wiki/Iris_flower_data_set
2. www.twofrog.com, Wild Iris - Iris Setosa.
http://www.twofrog.com/irissetosa.html
3. Fisher, R.A. (1936) The Use of Multiple measurements in Taxonomic Problems.
http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf
4. The University of Adelaide, Rare Books and Special Collections Sir Ronald Aylmer Fisher (1890-1962) Statistician and geneticist, Papers 1911-2005.
https://www.adelaide.edu.au/library/special/mss/fisher/
5. Pfeiffer, D (1994) Eugenics and Disability Discrimination, Disability & Society, 9:4, 481-499, DOI: 10.1080/09687599466780471
6. Galton, F. (1869) Hereditary Genius, 2nd edition, London and Colchester, Ballantyne & Co.
7. Shakespeare, T. (2008) ‘Disability, Genetics and Eugenics in Disability on equal terms’ in French S. & Swain J. (eds) Disability on Equal Terms, London: Sage Publications Ltd
8. Kerr, A. and Shakespeare, T. (2002) Genetic politics: from eugenics to genome, Cheltenham, New Clarion Press
9. Barnes, C. and Mercer, M. (2003) Disability, Cambridge: Polity Press
10. UCI Machine Learning Repository, Iris Data Set
https://archive.ics.uci.edu/ml/datasets/iris
11. A Multithreaded Software Model for Backpropgation Neural Network Applications, 2.4.1 Linear Separability and the XOR Problem
http://www.ece.utep.edu/research/webfuzzy/docs/kk-thesis/kk-thesis-html/node19.html
12. www.medium.com, The Linear Fischer Discriminant Analysis, A full introduction to The Linear Fisher Discriminant Analysis https://medium.com/@QuarizmiAdTech/a-full-introduction-to-the-linear-fisher-discriminant-analysis-848530dce336
13. BBC,  Bitesize Guides, KS3 Pattern recognition
https://www.bbc.com/bitesize/guides/zxxbgk7/revision/1
14. Math UMD, Example for Principal Component Analysis (PCA): Iris data
https://www.math.umd.edu/~petersd/666/html/iris_pca.html
15. Statistics How To, Percentiles, Percentile Rank & Percentile Range: Definition & Examples
https://www.statisticshowto.datasciencecentral.com/9. probability-and-statistics/percentiles-rank-range/
16. Pandas Documentation, 0.24.2 documentation, API Reference, Pandas Data Frame
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
17. Matplotlib Histogram – How to Visualize Distributions in Python 
https://asq.org/quality-resources/histogram#types
18. Machine Learning Mastery, Your First Machine Learning Project in Python Step-By-Step
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
19. Matplotlib Tutorial 5 - Histograms, Youtube
https://www.youtube.com/watch?v=r75BPh1uk38
20. Stackoverflow.com, Plotting histograms from grouped data in a pandas DataFrame 
https://stackoverflow.com/a/19603918/11250489
21. Stackoverflow.com, What is the difference between drawing plots using plot, axes or figure in matplotlib?
https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/37970713  
22. Wikipedia, Multimodal distribution.
https://en.wikipedia.org/wiki/Multimodal_distribution
23. Seaborn, Visualizing the distribution of a dataset
https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset
24. Datacamp, Community Tutorials, Python Seaborn Tutorial For Beginners.
https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#title
25. Seaborn, seaborn.pairplot.
https://seaborn.pydata.org/generated/seaborn.pairplot.html
26. Stackoverflow.com, How to add a title to Seaborn Facet Plot.
https://stackoverflow.com/questions/29813694/how-to-add-a-title-to-seaborn-facet-plot
27. Stackoverflow.com, How to control the legend in seaborn.
https://stackoverflow.com/questions/47542104/how-to-control-the-legend-in-seaborn-python
28. Pandas 0.24.2 documentation » API Reference » Series » pandas.Series » Value Counts. 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html
29. Pandas 0.24.2 documentation, API Reference, Series, Dataframes,Columns
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html?highlight=columns#pandas.DataFrame.columns 
30. Data36.com, Pandas Tutorial 1: Pandas Basics (Reading Data Files, DataFrames, Data Selection).
https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
31. Sharma, L. and  Sharma U. (2014) Neural Network Based Classifier (Pattern recognition) for
Classification of Iris Data Set, International Journal of Recent Development in Engineering and Technology Website: www.ijrdet.com  Volume 3, Issue 2, August 2014
https://pdfs.semanticscholar.org/1a6a/5b2be931799e1bf4b3d3e26d1b28446ff84f.pdf?_ga=2.43900261.1336379648.1556317383-327426060.1556317383