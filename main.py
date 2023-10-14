# -*- coding: utf-8 -*-
"""MallaOli_10915723_CC4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mIcGJCHzM7rB7dqKs8qPLfrDnJVEKpdB
"""

# libraries and frameworks
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# csv -> DataFrame
houseprice_df = pd.read_csv("houseprice_train.csv")

houseprice_df.head()

houseprice_df.corr()

houseprice_df.corr().iloc[-1,:].sort_values()

# features
print(houseprice_df[['GrLivArea']]) # +ve corr
print(houseprice_df[['YrSold']]) # -ve corr

##
# Simple Linear Model
##
X = houseprice_df[['GrLivArea']] # +ve corr
y = houseprice_df[['SalePrice']]
simple_model_saleVSlivarea = LinearRegression().fit(X,y)

# intercept, slope
print(f" Intercept: {simple_model_saleVSlivarea.intercept_[0]:.1f}\n",
      f"Slope: {simple_model_saleVSlivarea.coef_[0][0]:.1f}")

# visualization
y_predicted = simple_model_saleVSlivarea.predict(X)
plt.plot(X,y_predicted , c = 'red')
plt.scatter(X, y)
plt.show()

"""**Concept Part**
1. The correlation between "SalePrice" and "GrLivArea" shows a positive correlation of 0.71. The correlation strength is fairly high.
2. The slope of linear regression model between Living Area in X-axis and House Price in y-axis with a value of 107.1 can be interpreted as "the predicted cost of house price increases by $107.1 for every sq. foot of increase in the living area."
3. If I could add another feature to this already exsiting model or I would start with two features to work with, the "YrSold" or year the house was sold feature, which has a negative correlation with predicted house price. I think this would both of them combined, since they have opposite correlation strengths fitted with SalePrice, would help us see the complete picture.
4. Based on the data and based on the features we have selected, although I don't have much domain knowlege in this field as a student, I would recommend buying the house that has higher living space, since living space has high correlation with the predicted prices of the house. This could mean that the house could hold it's resell value or might be evaluated for higher sale in the future.
Since we have studied the correlation, houses that are old and having lower quality finish to avoid.
"""

##
# Bonus Coding Part
##
error = y - y_predicted
plt.axhline(y = 0, c = 'red', ls = "--")
plt.scatter(y_predicted, error)

# standard deviation
print(error.std())

