'''
Matplotlib
Baaki libraries matplotlib par hi bani hai
Types of Data-
Numerical Data - age,weight, temperature
Categorical Data - Data has groups . Eg phone brands, Branch of college
Analysis - Univariate,Bivariate or multivariate

Starting with 2d line plot
2d plot -> bivariate, 2 columns par apply hoga
* pehla column numerical ho, dusra column v numerical ho
* ek column numerical ho aur dusra column categorical ho
Use case -> Time series data (most popular)
            ek axis time hoga


'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
price = [48000,54000,57000,49000,47000,45000] # Numerical
year = [2015,2016,2017,2018,2019,2020] # Categorical
plt.plot(year,price)
plt.show()



