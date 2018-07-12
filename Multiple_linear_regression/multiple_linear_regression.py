# Importing dataset
import pandas as pd
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

# Encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x = LabelEncoder()
x[:,3] = labelEncoder_x.fit_transform(x[:,3])
oneHotEncoder = OneHotEncoder(categorical_features = [3])
x = oneHotEncoder.fit_transform(x).toarray()

# Avoiding the dummy varible trap
x = x[:,1:]

# Split dataset into training and test
from sklearn.model_selection import train_test_split #train_test_split is deprecated in cross_validation
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)

# Fitting multiple linear regression to trainning set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

# Prediction of test set results
y_pred = regressor.predict(x_test)

