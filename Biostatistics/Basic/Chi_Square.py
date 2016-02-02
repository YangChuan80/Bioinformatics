from scipy import stats
from pandas import DataFrame, Series
import numpy as np

df=DataFrame(np.array([68,6,52,11]).reshape(2,2))

chisquaretest_result=stats.chi2_contingency(df,correction=False)

print('Chi-Square test is: ',chisquaretest_result,'\n')