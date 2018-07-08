# Simple linear regression

# Import data
import pandas as pd
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

# Split train and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

# Fitting data into linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting x_test
y_pred = regressor.predict(x_test)

# Visualising the Training set results
import matplotlib.pyplot as plt
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Trainning Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Trainning Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Converting Linear Regression Model to CoreML Model
import coremltools
coreml_model = coremltools.converters.sklearn.convert(regressor)
coreml_model.author = "Karthik"
coreml_model.short_description = "Employee salary prediction using years of experience."
coreml_model.input_description["input"] = "Employee Experience"
coreml_model.output_description["prediction"] = "Employee Salary"
coreml_model.save("SalaryVsExperience.mlmodel")