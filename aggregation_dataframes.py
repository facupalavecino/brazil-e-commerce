import pandas as pd


def my_min(column):
    return column.min() + 28


order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv', index_col=0)

payment_values = order_payments['payment_value']

print(f"Payment Value's mean: {payment_values.mean()}")
print(f"Payment Value's median: {payment_values.median()}")
print(f"Payment Value's max: {payment_values.max()}")
print(f"Payment Value's min: {payment_values.min()}")
# The .agg() method allows us to compute a custom aggregation function defined by ourselves.
# It's possible to compute more than 1 function at once, passing an array of functions to the .agg() method
print(f"Payment Value's my min: {payment_values.agg(my_min)}")

# There are some Cumulative functions. These functions return a result for every row in the dataset
print(f"Payment Value's cumulative sum: {payment_values.cumsum()}]")
