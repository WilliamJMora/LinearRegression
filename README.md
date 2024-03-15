# LinearRegression
Linear Regression with Pandas, Excel, Matplotlib, Seaborn, and StatsModels

In this project, linear regression is applied to an American housing dataset to attempt to predict future housing prices and see if certain variables are more significant than others in given cities. Topics in this project include basic data cleaning with Microsoft Excel and Pandas and statistical analysis with Seaborn, Matplotlib, StatsModels, and Pandas.

## Contents:
1.  Housing dataset with Kaggle
2.	Data cleaning with Power Query and Pandas
3.	Dummy variables and categorical data
4.	Simple linear regression
5.	Correlation coefficients and heat maps with Seaborn
6.	Multiple linear regression and ordinary least squares with StatsModels
7.	Variation inflation factor
8.	Summary of analysis


### 1. Housing dataset with Kaggle

https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities/code

Linear regression is a supervised machine learning algorithm. Within supervised learning, there are classification and regression algorithms, with linear regression being in the latter category. Regression algorithms attempt to predict future data with known data as the input, as opposed to classification algorithms which try to label/classify data. 

Linear regression has a dependent variable that is affected by one or more independent variables. In this dataset the dependent variable is price while the independent variables are:
- Zip code
- Beds
- Baths
- Living space
- Address
- City
- State
- Zip code population
- Zip code density
- County
- Median household income
- Latitude
- Longitude

Not all of these variables will be used in the analysis as depicted during the cleaning of data.

### 2. Data cleaning with power query and Pandas

Before using the dataset, it is imperative to remove “dirty” data to ensure adequate analysis. Methods of data cleaning include:
- Handling missing data
- Removing duplicate data
- Removing irrelevant data
- Converting data types
- Fixing spelling mistakes
- Translating languages

There are more methods of cleaning data, but these are some of the most common techniques. Let’s apply these techniques to the housing dataset.

Cleaning data can be done in various mediums. First, the data will be cleaned in power query just to see how it can be used and completed in Microsoft Excel. Then, the same process will be shown using Pandas in Python. SQL is another tool that can be used. Choosing the platform to clean data can depend on multiple variables, such as how the data is stored and just personal preference.

To start, get the data in Microsoft Excel after downloading the CSV file from Kaggle through Power Query (located in the Data tab).


