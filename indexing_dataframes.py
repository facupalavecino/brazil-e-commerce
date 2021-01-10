import pandas as pd

order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv', index_col=0)

'''
A pandas DF is composed by 3 parts:
- 1x 2DNumPy array containing the values
- 2x Indexes representing the columns and rows
'''