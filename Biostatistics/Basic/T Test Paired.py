from scipy import stats

ap=Series([113,125,126,130,150,145,135,105,128,135,100,130,110,115,120,155])
bp=Series([140,150,138,120,140,145,135,115,135,130,120,133,147,125,114,165])

paired_ttest=stats.ttest_rel(bp,ap)

print('T-Test of paired sample is: ', paired_ttest)
