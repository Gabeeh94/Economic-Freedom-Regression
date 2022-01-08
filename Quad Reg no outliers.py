import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (11, 5)  #set default figure size
import numpy as np
import pandas as pd
import statsmodels.api as sm

#Detect and deletes outliers in the scores using the Inter Quartile Range
def delete_outliers (var):
    Q1 = np.percentile(scores_GDP[var], 25, interpolation = 'midpoint')
    Q3 = np.percentile(scores_GDP[var], 75, interpolation = 'midpoint')
    IQR = Q3-Q1 
    #Above Upper Bound
    upper = scores_GDP.index[scores_GDP[var] >= (Q3 + 1.5*IQR)]
    #Below Lower Bound
    lower = scores_GDP.index[scores_GDP[var] <= (Q1 - 1.5*IQR)]
    #Drops outliers
    scores_GDP.drop(upper, inplace = True)
    scores_GDP.drop(lower, inplace = True)
    
#Reads data and assigns it to a pandas' dataframe

df = pd.read_excel('/home/gabriel/Documents/index2021_data.xls','Sheet1', index_col=None, na_values=['N/A'])

#Takes the scores and GDP per capita variables and creates a sub dataframe

scores_GDP = df[['Country Name','2021 Score','GDP per Capita (PPP)']].copy(deep=True)

if scores_GDP.isnull().any().any() == True:  #Checks is there are any null values in the dataframe
    scores_GDP_with_nan = scores_GDP.index[scores_GDP.isnull().any(axis=1)] #Creates dataframe with countries with null values
    scores_GDP.drop(scores_GDP_with_nan, 0, inplace = True) #Deletes countries without rows

#Create a scatterplot to see if there is a relationship in the data

plt.scatter(scores_GDP['2021 Score'], scores_GDP['GDP per Capita (PPP)'])

delete_outliers('2021 Score')
delete_outliers('GDP per Capita (PPP)')

#Create a scatterplot without the outliers

plt.scatter(scores_GDP['2021 Score'], scores_GDP['GDP per Capita (PPP)'])

#Adds another column with the score values squared to make a quadratic regression
scores_GDP['2021 Score Square'] = scores_GDP['2021 Score']**2 

x = scores_GDP[['2021 Score','2021 Score Square']] #Independent Variable, explains the y

y = scores_GDP['GDP per Capita (PPP)'] #Dependent Variable, we want to explain it



model = sm.OLS(y, x).fit()


# Plot a graph showing the regression

plt.style.use('seaborn')

# Plot predicted values

predictions = model.predict(x) # make the predictions by the model
fix, ax = plt.subplots()
ax.scatter(scores_GDP['2021 Score'], predictions, alpha=0.5,
        label='predicted')

# Plot observed values

ax.scatter(scores_GDP['2021 Score'], scores_GDP['GDP per Capita (PPP)'], alpha=0.5,
        label='observed')

#Configure and show graph

ax.legend()
ax.set_title('OLS predicted values')
ax.set_xlabel('2021 Score')
ax.set_ylabel('GDP per Capita (PPP)')
plt.show()

#Define figure size
fig = plt.figure(figsize=(12,8))

#Produce regression plots
fig = sm.graphics.plot_regress_exog(model,'2021 Score' , fig=fig)

# Print out the statistics
print(model.summary())
