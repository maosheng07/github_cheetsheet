import pandas as pd
import numpy as np

'''
Example script taken from https://pandas.pydata.org/pandas-docs/stable/10min.html
'''
# Make an array with six dates and 4 arbitrary random numbers as 'observations'
dates = pd.date_range('20130101', periods=6)
# Parse into a pandas dataframe
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# print the short data frame to stdout
print(df)
print("completed")
