import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import numpy as np

# read csv
data = pd.read_csv('data.csv')

# data cleaning
pd.options.mode.chained_assignment = None
data.drop(['Address', 'Latitude', 'Longitude'], axis=1, inplace=True)
data.drop_duplicates()
data.dropna()

# selecting subset
subset_data = data[data['City'] == 'Flushing']

# creating dummy variables
subset_data = pd.get_dummies(subset_data, columns=['Zip_Code'], dtype='int')
# removing categorical data
subset_data.drop(['City', 'State', 'County'], axis=1, inplace=True)
# removing dummy variable
subset_data.drop(['Zip_Code_11367'], axis=1, inplace=True)

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

# correlation coefficients
correlation = subset_data.corr(method='pearson')
print(correlation)

# heat map of coefficients
sb.heatmap(correlation, annot=True)
plt.show()

# ordinary least squares
ols = sm.ols(formula='Price ~ Beds + Baths + Living_Space + Zip_Code_Population + Zip_Code_Density + Median_Household_Income', data=subset_data)
model = ols.fit()
print(model.summary())
