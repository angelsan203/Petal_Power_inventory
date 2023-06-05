import codecademylib3
import pandas as pd
import numpy as np

inventory = pd.read_csv('inventory.csv')
print(inventory)

staten_island = inventory[inventory['location'] == 'Staten Island']
print(staten_island)

product_request = staten_island['product_description']
print(product_request)

seed_request = inventory.loc[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
print(seed_request)

inventory['in_stock'] = np.where(inventory['quantity'] > 0, True, False)
print(inventory)

inventory['total_value'] = round(inventory['price'] * inventory['quantity'],2)
print(inventory)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)
