# Map Reduce with Python's mrjob Library

In this repository are some small-scale programs that utilize MapReduce,
a programming paradigm for big data processing, to read, analyze, and process
data in certain ways. They rely on python's mrjob library. 

## pattern_processing.py
This program reads the Iris Data Set from UCI's machine learning repository and produces
several outputs. It finds the minimum sepal length, the maximum petal width, 
the average sepal width for the class “Iris Setosa”, 
and the difference in average sepal and petal length for all non-“Iris Setosa”.

It's a one-step mrjob program with one mapper and one reducer. The last output is
little more intricate in difficulty than the first three, as it utilizes
a tuple as value and execute calculations on members of the tuple. 

To run the program: 
```
python3 pattern_processing.py iris.data
```

## wordsearch.py
A simple program to find certain words with regex. It can be tweaked easily
to take inputs from command line, which it currently does not.
```
python3 pattern_processing.py harry.txt
```

## A simple program to find the top 10 most frequently appeared words in a text.
```
python3 highfrequencywords.py harry.txt
```

## Run jobs on Elastic MapReduce and Use S3 with AWS
Configurations can be found in file ```mrjob.conf```. 
To run on EMR:
```markdown
python highfrequencywords.py -r emr --conf-path ./mrjob.conf harry.txt
```
I deleted my testing AWS access keys, so it can't be run anymore, but here's a screenshot of 
expected result.
![](elastic_mapreduce_result(1).png)
![](elastic_mapreduce_result(2).png)

## word_frequency.py and mr_word_count.py
As indicated by their citations, they are sample programs from mrjob's documentation.

