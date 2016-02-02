from scipy import stats
from pandas import DataFrame, Series

a=Series([6.2, 3.7, 5.8, 2.7, 3.9, 6.1, 6.7, 7.8, 3.8, 6.9])
b=Series([8.5, 6.8, 11.3, 9.4, 9.3, 7.3, 5.6, 7.9, 7.2, 8.2])

ap=Series([113,125,126,130,150,145,135,105,128,135,100,130,110,115,120,155])
bp=Series([140,150,138,120,140,145,135,115,135,130,120,133,147,125,114,165])

random_ttest=stats.ttest_ind(a,b)
paired_ttest=stats.ttest_rel(bp,ap)

print('T-Test of random sample is: ', random_ttest)
print('T-Test of paired sample is: ', paired_ttest)
