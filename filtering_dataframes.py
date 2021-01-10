import pandas as pd
import numpy as np

# Get a DataFrame from a CSV file
order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv', index_col=0)

# Returns True or False if the row meets the conditions. I'm not selecting any rows
print(np.logical_and(order_payments['payment_value'] > 700, order_payments['payment_value'] < 800))

# Returns the entire rows that meet the conditions. I'm seleting the rows based on the conditions
filtered_payments = order_payments[np.logical_and(order_payments['payment_value'] > 700, order_payments['payment_value'] < 800)]
print(filtered_payments)

# I can iterate a Pandas DataFrame with iterrows()
for lab, row in filtered_payments.iterrows():
    print(f'{lab}')
    print(row)
