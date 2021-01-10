import pandas as pd

# Get a DataFrame from a CSV file
order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv', index_col=0)

# head() returns the first n rows of the dataset
print(order_payments.head())
# tail() returns the last n rows of the dataset by position
print(order_payments.tail(3))

# info() gives us information about data types contained, amount of missing values, etc
print(order_payments.info())

# shape returns the Matrix size of the dataset
print(order_payments.shape)

# describe() returns some insights about the dataset, such as count/mean/std/min value/max value/...
print(order_payments.describe())

# .values returns a NumPy 2D array with the dataset information
print(order_payments.values)

# .columns returns an Index of columns: their names
cols = order_payments.columns

# .index returns an index for the rows: either their position or tags
# An Index is kind of a list of numbers or strings, but it allows more sophisticated processing
row_index = order_payments.index
