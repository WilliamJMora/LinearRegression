# LinearRegression
Linear Regression with Pandas, Excel, Matplotlib, Seaborn, StatsModels, and NumPy

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

There are more methods of cleaning data, but these are some of the most common techniques. Let's apply these techniques to the housing dataset.

Cleaning data can be done in various mediums. First, the data is cleaned in power query just to show how it can be used and completed in Microsoft Excel. Then, the same process will be shown using Pandas in Python. SQL is another tool that can be used. Choosing the platform to clean data can depend on multiple variables, such as how the data is stored, the size of the dataset (this is where Excel is limited compared to SQL, Pandas, etc.), and just personal preference.

To start, let's get the data in Microsoft Excel after downloading the CSV file from Kaggle through Power Query (located in the **Data** tab).

### Power Query 1

Let's select **Get Data (Power Query)**.

### Power Query 2

Data can be imported from various sources. Since the dataset is in a CSV file, let's select **Text/CSV**.

### Power Query 3

After that, the data needs to be cleaned before loading it into Excel, so **Transform Data** is selected.

### Power Query 4

This opens up Power Query and displays the data. On the right, there is a running log of all the changes made. This is how to undo a change.

### Power Query 5

First, let’s handle missing data. When sorting by ascending median household income, two null values are uncovered.

### Power Query 6

### Power Query 7

There are different ways of handling missing data. This includes replacing it with sensible data, such as the mean, and removing/filtering out the data. Since this dataset is large, removing two entries will not have any major repercussions for the end results. In the home tab, let’s select **Remove rows**, **Remove top rows**, then enter 2 to remove the unwanted data. 

### Power Query 8

Now, let’s remove duplicate data. This is done simply by selecting **Remove rows** and **Remove duplicates**.

### Power Query 9

Next, let’s get rid of irrelevant data. It is important to be sure that the data that is being removed is not important so the analysis can be accurate. Removing important data will have unwanted effects on prediction. Common sense is critical in data analysis.

The columns of **Zip Code**, **City**, **State**, and **County** should be kept as they have geographical importance to the data. However, the individual address of each house is not important. Also, latitude and longitude might have effects on the data, but there are better methods to handling these points. Therefore, **Address**, **Latitude**, and **Longitude** can be removed. A column can be removed by selecting it and then choosing Remove columns. 

### Power Query 10

The remaining data, **Beds**, **Baths**, **Living space**, **Zip code population**, **Zip code density**, and **Median household income**, can affect prices, so these columns should be kept.

Looking at the data types, only **Zip code** needs to be changed. Zip codes represent geographical areas and the computer will interpret them as numbers since they consist of digits and higher zip codes will be treated as if they are worth more. Therefore, let's change **Zip Code** from a numberical data type to a text data type.

### Power Query 11

### Power Query 12

### Power Query 13

Let’s change the column names that have more than one word by putting a line between the words (Zip Code to Zip_Code). This is important for when it is time to access columns in Pandas. The names can be changed by double clicking the column names.

### Power Query 14

Let's load the data into an Excel table by clicking **Close & Load**.

### Power Query 15

The dataset can be saved as an Excel spreadsheet or a CSV file and imported into the project (delete any other sheets, such as Sheet1).

Before moving on, let's clean the data in a CSV file with Pandas.

```
# importing modules
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np

# read csv
data = pd.read_csv('data.csv')

# data cleaning
# this just removes the error given when copying a dataframe
pd.options.mode.chained_assignment = None
# removing the Address, Latitude, and Longitude columns (series)
data.drop(['Address', 'Latitude', 'Longitude'], axis=1, inplace=True)
# removing duplicates
data.drop_duplicates()
# removing rows with NaN (null values)
data.dropna()
```

### 3. Categorical data and dummy variables

As aforementioned, we changed **Zip_Code** to a text data type since it is categorical data. Another example would be the four cardinal directions (North, South, East, and West). If we just assigned numbers one through four to them, the directions with higher numbers would be worth more value, but in reality, they are all worth the same. Let's create four dummy variables.

Old Table

| Direction |
|-----------|
| North     |
| South     |
| West      |
| North     |
| East      |
| West      |
| South     |
| East      |

New Table

| North_x1 | South_x2 | East_x3 | West_x4 |
|----------|----------|---------|---------|
| 1        | 0        | 0       | 0       |
| 0        | 1        | 0       | 0       |
| 0        | 0        | 0       | 1       |
| 1        | 0        | 0       | 0       |
| 0        | 0        | 1       | 0       |
| 0        | 0        | 0       | 1       |
| 0        | 1        | 0       | 0       |
| 0        | 0        | 1       | 0       |

We divide the four variables into their own column and put a 1 where the row from the old table corresponds with the direction. Now, the four directions all have the same value. We would get rid of one of the columns when running linear regression to avoid multicollinearity (correlation between two independent variables).

For our example with the housing dataset, we can do this for our zip codes. If there are too many though, it could cause more of a hindrance than help considering all of the columns. If we are only looking at houses in a single zip code for prediction, then there would be no need to create dummy variables.

Also, it is important to note that removing columns and multicollinearity is not necessary when trying to predict future values, rather than trying to see which independent variables have the strongest effects on the dependent variable.

### 4. Simple linear regression

Let's analyse the houses in Flushing, New York.

```
# selecting subset
subset_data = data[data['City'] == 'Flushing']
```

```
     Zip_Code    Price  Beds  ...  Zip_Code_Density  County Median_Household_Income
429     11354   598000     1  ...            9577.8  Queens                   84204
430     11354   973000     2  ...            9577.8  Queens                   84204
431     11354   658888     2  ...            9577.8  Queens                   84204
432     11354   874000     2  ...            9577.8  Queens                   84204
433     11354   638000     1  ...            9577.8  Queens                   84204
434     11354   339000     2  ...            9577.8  Queens                   84204
435     11354   742000     1  ...            9577.8  Queens                   84204
436     11354   880000     2  ...            9577.8  Queens                   84204
437     11354   551000     1  ...            9577.8  Queens                   84204
438     11354   655000     1  ...            9577.8  Queens                   84204
439     11354   258000     1  ...            9577.8  Queens                   84204
440     11354   566000     1  ...            9577.8  Queens                   84204
441     11354   818000     2  ...            9577.8  Queens                   84204
442     11354   640200     1  ...            9577.8  Queens                   84204
443     11354  2128000     7  ...            9577.8  Queens                   84204
444     11354   359000     1  ...            9577.8  Queens                   84204
445     11354   677000     1  ...            9577.8  Queens                   84204
446     11354   618000     1  ...            9577.8  Queens                   84204
447     11354   749000     2  ...            9577.8  Queens                   84204
448     11354   299000     1  ...            9577.8  Queens                   84204
449     11354   308000     1  ...            9577.8  Queens                   84204
450     11354   899999     3  ...            9577.8  Queens                   84204
451     11354   298000     2  ...            9577.8  Queens                   84204
452     11354   585000     1  ...            9577.8  Queens                   84204
453     11354   988000     2  ...            9577.8  Queens                   84204
454     11354   899999     3  ...            9577.8  Queens                   84204
455     11355  2980000    14  ...           18200.0  Queens                   77413
456     11355   485000     1  ...           18200.0  Queens                   77413
457     11355   525000     1  ...           18200.0  Queens                   77413
458     11355   550000     2  ...           18200.0  Queens                   77413
471     11358   728000     2  ...            7518.7  Queens                  109224
472     11358  1898000     5  ...            7518.7  Queens                  109224
473     11358   880000     3  ...            7518.7  Queens                  109224
474     11358  2600000     6  ...            7518.7  Queens                  109224
506     11367   488000     1  ...            8553.5  Queens                  101917
507     11367   399000     2  ...            8553.5  Queens                  101917
508     11367   375000     2  ...            8553.5  Queens                  101917
509     11367   388000     2  ...            8553.5  Queens                  101917
510     11367   408000     1  ...            8553.5  Queens                  101917
511     11367   408000     1  ...            8553.5  Queens                  101917

[40 rows x 11 columns]
```

The ellipses denote that there is hidden data.

Next, let's create the zip code dummy variables. There are four zip codes (11354, 11355, 11358, and 11367), so there will be three dummy variables. Also, we can remove the categorical data so there are no errors.

```
# creating dummy variables
subset_data = pd.get_dummies(subset_data, columns=['Zip_Code'], dtype='int')

# removing categorical data
subset_data.drop(['City', 'State', 'County'], axis=1, inplace=True)
```

```
       Price  Beds  Baths  ...  Zip_Code_11355  Zip_Code_11358  Zip_Code_11367
429   598000     1      1  ...               0               0               0
430   973000     2      2  ...               0               0               0
431   658888     2      2  ...               0               0               0
432   874000     2      1  ...               0               0               0
433   638000     1      1  ...               0               0               0
434   339000     2      1  ...               0               0               0
435   742000     1      1  ...               0               0               0
436   880000     2      2  ...               0               0               0
437   551000     1      1  ...               0               0               0
438   655000     1      1  ...               0               0               0
439   258000     1      1  ...               0               0               0
440   566000     1      1  ...               0               0               0
441   818000     2      2  ...               0               0               0
442   640200     1      1  ...               0               0               0
443  2128000     7      5  ...               0               0               0
444   359000     1      1  ...               0               0               0
445   677000     1      1  ...               0               0               0
446   618000     1      1  ...               0               0               0
447   749000     2      2  ...               0               0               0
448   299000     1      1  ...               0               0               0
449   308000     1      1  ...               0               0               0
450   899999     3      3  ...               0               0               0
451   298000     2      1  ...               0               0               0
452   585000     1      1  ...               0               0               0
453   988000     2      2  ...               0               0               0
454   899999     3      3  ...               0               0               0
455  2980000    14      8  ...               1               0               0
456   485000     1      1  ...               1               0               0
457   525000     1      1  ...               1               0               0
458   550000     2      1  ...               1               0               0
471   728000     2      1  ...               0               1               0
472  1898000     5      5  ...               0               1               0
473   880000     3      2  ...               0               1               0
474  2600000     6      7  ...               0               1               0
506   488000     1      1  ...               0               0               1
507   399000     2      1  ...               0               0               1
508   375000     2      1  ...               0               0               1
509   388000     2      1  ...               0               0               1
510   408000     1      1  ...               0               0               1
511   408000     1      1  ...               0               0               1

[40 rows x 11 columns]
```

Before running multiple linear regression, let's look at how each independent variable interacts with price, the dependent variable. Simple linear regression has one independent and one dependent variable. To make predictions, the method of least squares is used to find the line of best fit which minimizes the distance between itself and all of the data points.

The math behind the method can be found here:
https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit

```
# simple linear regression
x1 = subset_data['Beds']
x2 = subset_data['Baths']
x3 = subset_data['Living_Space']
x4 = subset_data['Zip_Code_Population']
x5 = subset_data['Zip_Code_Density']
x6 = subset_data['Median_Household_Income']
y_axis = subset_data['Price']
plt.title("Price vs. Beds")
plt.xlabel("Beds")
plt.ylabel("Price")

x, y = np.polyfit(x1, y_axis, 1)
plt.scatter(x1, y_axis)
plt.plot(x1, x*x1 + y)
plt.show()
```

### Flushing Graphs ###

By looking at the graphs, it looks like beds, baths, and living space could have the strongest relations to price. This means that they may be kept for a linear regression equation.

### 5. Correlation coefficients and heat map with Seaborn

The correlation coefficient measures the strength of linear correlation between two variables. Using Pandas, let's find the correlation coefficients amongst all of the independent variables in the Flushing housing dataset.

```
# correlation coefficients
correlation = subset_data.corr(method='pearson')
```

```
                            Price      Beds  ...  Zip_Code_11358  Zip_Code_11367
Price                    1.000000  0.896970  ...        0.421833       -0.260449
Beds                     0.896970  1.000000  ...        0.259161       -0.127014
Baths                    0.964373  0.917656  ...        0.398541       -0.206056
Living_Space             0.777290  0.644620  ...        0.692711       -0.170555
Zip_Code_Population      0.069691  0.189211  ...       -0.457154       -0.410863
Zip_Code_Density         0.127505  0.266648  ...       -0.306482       -0.230225
Median_Household_Income  0.114257  0.048143  ...        0.705415        0.572746
Zip_Code_11354          -0.196924 -0.276202  ...       -0.454257       -0.572478
Zip_Code_11355           0.201253  0.331150  ...       -0.111111       -0.140028
Zip_Code_11358           0.421833  0.259161  ...        1.000000       -0.140028
Zip_Code_11367          -0.260449 -0.127014  ...       -0.140028        1.000000
```

The correlation coefficient ranges from -1 to 1. The closer the number is to -1 or 1, the stronger the correlation between the two variables.

This information can be displayed in a Seaborn heat map.

```
# heat map of coefficients
sb.heatmap(correlation, annot=True)
plt.show()
```

### Heat Map ###

By looking at the heat map, we can see that there are some strong correlations, including:
- Zip code density and zip code 11355
- Zip code density and zip code population
- Beds and baths

This means that some of these variables could be removed from our dataset to reduce multicollinearity. Multicollinearity is the strength of correlation between two independent variables. Stronger multicollinearity can reduce the accuracy of the model. More observation is needed before removing any variables.

### 6. Multiple linear regression and ordinary least squares with StatsModels

By using ordinary least squares, we can choose which variables are suitable for the model. Let's run OLS on the Flushing housing dataset.

```
# ordinary least squares
ols = sm.ols(formula='Price ~ Beds + Baths + Living_Space + Zip_Code_Population + Zip_Code_Density + Median_Household_Income', data=subset_data)
model = ols.fit()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  Price   R-squared:                       0.943
Model:                            OLS   Adj. R-squared:                  0.933
Method:                 Least Squares   F-statistic:                     91.02
Date:                Sat, 16 Mar 2024   Prob (F-statistic):           4.28e-19
Time:                        18:44:56   Log-Likelihood:                -531.08
No. Observations:                  40   AIC:                             1076.
Df Residuals:                      33   BIC:                             1088.
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
Intercept               -1.185e+07   4.66e+06     -2.542      0.016   -2.13e+07   -2.36e+06
Beds                     1.708e+04    3.3e+04      0.518      0.608      -5e+04    8.41e+04
Baths                    3.646e+05   6.41e+04      5.689      0.000    2.34e+05    4.95e+05
Living_Space             -165.5349     99.661     -1.661      0.106    -368.296      37.226
Zip_Code_Population       196.6046     75.920      2.590      0.014      42.145     351.064
Zip_Code_Density         -566.9071    218.555     -2.594      0.014   -1011.560    -122.254
Median_Household_Income    83.5432     32.458      2.574      0.015      17.507     149.580
==============================================================================
Omnibus:                        1.429   Durbin-Watson:                   2.120
Prob(Omnibus):                  0.489   Jarque-Bera (JB):                0.854
Skew:                           0.353   Prob(JB):                        0.652
Kurtosis:                       3.114   Cond. No.                     1.97e+07
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.97e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
```

The null hypothesis states that there is no substantial relationship between variables. By reading the statistics above, we can see if we can reject the null hypothesis.

The first value to look at is adjusted R-squared. Adjusted R-squared ranges from 0 to 1 with a higher number indicating that the model is possibly a good fit for the data. However, the number does not give insight into whether it is good for prediction. At, .933, 93.3% of the variation in price can be explained by the independent variables. The model above is a good fit for the data.

