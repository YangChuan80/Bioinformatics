from scipy import stats
from pandas import DataFrame, Series
import numpy as np

a=Series([6.2, 3.7, 5.8, 2.7, 3.9, 6.1, 6.7, 7.8, 3.8, 6.9])
b=Series([8.5, 6.8, 11.3, 9.4, 9.3, 7.3, 5.6, 7.9, 7.2, 8.2])

ap=Series([113,125,126,130,150,145,135,105,128,135,100,130,110,115,120,155])
bp=Series([140,150,138,120,140,145,135,115,135,130,120,133,147,125,114,165])

ttest_result1=stats.ttest_ind(a,b)
ttest_result2=stats.ttest_rel(bp,ap)

arr=DataFrame([[442,483,416,172],[369,384,487,115]])

chisquaretest_result=stats.chi2_contingency(arr,correction=False)

x=[47.7, 34.5, 41.6, 34.1, 36.3, 45.2, 49.2, 34.0, 44.2, 40.5, 41.5, 32.2]
y=[49.7, 57.2, 48.3, 59.1, 47.7, 57.5, 56.6, 50.5, 56.7, 43.5, 51.8, 56.9]
z=[84.4, 70.1, 68.0, 73.7, 75.5, 80.3, 82.9, 79.1, 63.2, 71.1, 69.6, 72.4]

anova_result=stats.f_oneway(x,y,z)

print('Chi-Square test is: ',chisquaretest_result,'\n')
print('T test is: ',ttest_result1,'\n')



