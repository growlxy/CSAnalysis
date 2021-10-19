# Data Analysis of [Lagou Job](http://www.lagou.com/)

## Introduction
This is my first relatively complete repository, which holds the code of crawling [Lagou](http://www.lagou.com/) and job data for analysis
The main functions included are listed as follows: 

1. Crawling job details info from [Lagou](www.lagou.com).
2. Combining static login cookie and dynamic cookie are used to spider strategy.
3. The csv of data.
4. Generating word cloud.

## Prerequisites
Install 3rd party libraries  
```sudo pip3 install -r requirements.txt```

## How to Use
1. clone this repository from [github](https://github.com/growlxy/CSAnalysis).
2. run 
``` 
word = '' # key word
getData(word)
```
it will generate a collection of csv files in ```./analysis``` directory.
3. run 
``` 
word = '' # key word
create_pic(word)
```
it will return __TOP-50__ hot words and wordcloud figure(if you need, cheak the code and save the image).

## Thanks
(https://github.com/lucasxlu/LagouJob)

## LICENSE
[Apache-2.0](./LICENSE)