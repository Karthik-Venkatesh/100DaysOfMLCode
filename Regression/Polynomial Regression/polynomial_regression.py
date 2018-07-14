# Polynomial Regression

# Importing the dataset
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
#We dont need a position the Categorical variableTo construct matrix we are giving the range of level instead of index of level
x = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values

# Fit linear polynomial to the dataset. For more accurate changing(increasing) the degree
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg = LinearRegression()
lin_reg.fit(x_poly,y)

# Visualizing the polynomial regression results
import matplotlib.pyplot as plt
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualizing the polynomial regression results
# Below we drew prediction curve on 1,1.1,1.2...10
# Before it was 1,2,3...10
import numpy as np
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, lin_reg.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Predicting The Resluts
# polynomial regression
lin_reg.predict(poly_reg.fit_transform(6.5))