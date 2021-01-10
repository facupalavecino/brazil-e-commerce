import pandas as pd

# Get a DataFrame from a CSV file
order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv', index_col=0)

cols = order_payments.columns

# .sort_values() let us sort the dataset by 1 or more columns, asc or desc
order_payments_val = order_payments.sort_values('payment_value', ascending=False)
order_payments_type_val = order_payments.sort_values(['payment_type', 'payment_value'], ascending=[False, True])

print(order_payments_type_val.head(10))

# I can subset a dataset by accessing specific columns or rows
just_payment_values = order_payments['payment_value']

# I can filter a DataFrame by setting conditionals to the indexing
payment_values_above_2k = just_payment_values[just_payment_values > 2000]

print(payment_values_above_2k)

# The isin() method allow us to perform a logical | operation to filter the dataset.
order_payments_cr_vc = order_payments[order_payments['payment_type'].isin(['voucher', 'credit_card'])]

print(order_payments_cr_vc)
